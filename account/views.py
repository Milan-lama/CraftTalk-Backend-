from django.shortcuts import render
from .models import CustomUser
from rest_framework.views import APIView
from .serializer import UserSerializers, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserApi(APIView):
    permission_classes = [AllowAny]  # Default permission for GET requests

    def get(self, request):
        try:
            data = CustomUser.objects.filter(is_superuser=False)
            serializer = UserSerializers(data, many=True)
            print(serializer.data)
            return Response({'status': True, 'data': serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': f'An error occurred: {e}'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        
        try:
            data = request.data
            serializer = UserSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Account created successfully',
                }, status.HTTP_201_CREATED)
            return Response({'status': False, 'message': serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': f'An error occurred: {e}'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        print(request.data)
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': serializer.errors
                }, status.HTTP_400_BAD_REQUEST)
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username,password)
            # Use authenticate to validate credentials
            user = authenticate(username=username, password=password)

            print(user.id)
            if not user:
                return Response({
                    'status': False,
                    'message': 'Invalid credentials'
                }, status.HTTP_400_BAD_REQUEST)
            
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'status': True,
                'message': 'User logged in',
                'id':user.id,
                'username':user.username,
                'token': token.key
            }, status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'An error occurred: {e}',
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)
