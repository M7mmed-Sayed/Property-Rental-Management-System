from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from ..models import User

@api_view(['POST'])
def login(request):
    password=request.data.get("password",None)
    email=request.data.get("email",None)
    print(password)
    print(email)
    login_user = authenticate(email=email, password=password)
    if login_user is None:
        return Response({"messsage" :"wrong pass or user name"}, status=status.HTTP_400_BAD_REQUEST)
   
    token, _ = Token.objects.get_or_create(user=login_user)
    user = User.objects.get(email=email)
    response={
        'id':user.id,
        'email':user.email,
        'username':user.username,
        'token': token.key
        }
    
    return Response({"message": response}, status=status.HTTP_200_OK)

