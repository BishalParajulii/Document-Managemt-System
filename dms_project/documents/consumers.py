from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .models import Document, DocumentContent
from .utils import can_edit, can_view

class DocumentConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.doc_id = self.scope['url_route']['kwargs']['doc_id']
        self.room_group_name = f"document_{self.doc_id}"

        self.document = await sync_to_async(Document.objects.get)(id=self.doc_id)

        # Allow view OR edit to connect
        allowed = await sync_to_async(can_view)(self.scope["user"], self.document)
        if not allowed:
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive_json(self, content):
        await self.send_json({
            "message": content["content"]
        })


    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get("content", "")

        # Only editors can update
        if not await sync_to_async(can_edit)(self.scope["user"], self.document):
            return

        doc_content, _ = await sync_to_async(
            DocumentContent.objects.get_or_create
        )(document=self.document)

        doc_content.content = content
        doc_content.last_edited_by = self.scope["user"]
        await sync_to_async(doc_content.save)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "document_update",
                "content": content,
                "user": self.scope["user"].username,
            }
        )

    async def document_update(self, event):
        await self.send(text_data=json.dumps({
            "content": event["content"],
            "user": event["user"],
        }))
