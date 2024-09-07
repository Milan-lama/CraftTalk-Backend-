from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import MessageSerializer
from .models import Messages
from .middlewares import get_user
from rest_framework.authtoken.models import Token
from django.db.models import Q
class ShowMessages(APIView):
    def get(self, request,reciever=None):
        try:
            # reciever = request.GET.get('reciever')
            print(reciever)
            # Access token from the Authorization header
            auth_header = request.headers.get('Authorization')
            token = None
            if auth_header:
                token = auth_header.split()[1]  # Extract the token part
            print(token)    

            # Fetch the user from the token
            sender = Token.objects.get(key=token)
            sender_username = sender.user.username
            # Fetch messages based on the sender and receiver
            data = Messages.objects.filter(Q(reciever=reciever, sender=sender_username) |Q(reciever=sender_username, sender=reciever))
            print(data)
            # Serialize the messages
            serializer = MessageSerializer(data, many=True)
            print(serializer.data)
            # Return a response with the serialized data
            return Response({'status': True, 'data': serializer.data}, status.HTTP_200_OK)

        


        except Exception as e:
            # Return a 500 error if something goes wrong
            return Response({
                'status': False,
                'message': f'Error: {e}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
