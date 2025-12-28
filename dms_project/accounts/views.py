from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self , request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message" : "user Registered Successfully"},
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.error , status = status.HTTP_400_BAD_REQUEST)