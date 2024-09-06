import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Messages
from channels.db import database_sync_to_async
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope.get('user')
        url_username  = self.scope['url_route']['kwargs']['username']
        if user is None or user.is_anonymous or url_username != user.username:
            self.close(code=403)
        else:
            self.username = user.username
            self.room_group_name = f'chat_{self.username}'
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['Text']
        recipient = text_data_json['recipient']
        recipient_group_name = f'chat_{recipient}'
        message_id,sender,reciever = async_to_sync(self.save_to_db)(
            recipient=recipient,
            text=message,
            sender=self.username
        )
        async_to_sync(self.channel_layer.group_send)(
            recipient_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'id':message_id,
                'sender':sender,
                'reciever':reciever
            }
        )

    def chat_message(self, event):
        message = event['message']
        message_id = event['id']
        sender = event['sender']
        reciever = event['reciever']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'text': message,
            'id':message_id,
            'sender':sender,
            'reciever':reciever
        }))
    @database_sync_to_async
    def save_to_db(self,recipient,text,sender):
        message = Messages.objects.create(
            sender=sender,
            reciever=recipient,
            text=text
        )
        return (message.id,message.sender,message.reciever)
