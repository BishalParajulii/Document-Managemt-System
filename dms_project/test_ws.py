import os
import django
import asyncio

# BOOTSTRAP DJANGO
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from channels.testing import WebsocketCommunicator
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from documents.models import Document
from config.asgi import application


async def test_ws():
    user = await sync_to_async(User.objects.first)()
    doc = await sync_to_async(Document.objects.first)()

    if not user or not doc:
        print("❌ Create at least one user and document first")
        return

    communicator = WebsocketCommunicator(
        application,
        f"/ws/documents/{doc.id}/"
    )
    communicator.scope["user"] = user

    connected, _ = await communicator.connect()
    print("Connected:", connected)

    await communicator.send_json_to({"content": "Hello live edit"})
    response = await communicator.receive_json_from()
    print("Received:", response)

    await communicator.disconnect()


asyncio.run(test_ws())
