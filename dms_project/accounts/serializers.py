from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    group = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['username' , 'password' , 'group']
        
    def validate_username(self , value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value
    
    def validate_group(self, value):
        if not Group.objects.filter(name=value).exists():
            raise serializers.ValidationError("Invalid group")
        return value
            
        
    def create(self, validated_data):
        group_name = validated_data.pop('group')
        password = validated_data.pop('password')
        
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        
        return user
    



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls , user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
    def validate(self, attrs):
        data =  super().validate(attrs)
        data['username'] = self.user.username
        return data
    