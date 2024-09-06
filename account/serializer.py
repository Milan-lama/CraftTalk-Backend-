from rest_framework import serializers
from .models import CustomUser
import regex as re
class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username','first_name', 'last_name','password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
        }
    
    def validate(self,data):
        pattern = r'[^a-zA-Z0-9\s]'
        if re.search(pattern,data['first_name']):
            raise serializers.ValidationError('Name should Contain any shymbols')
        if re.search(pattern,data['last_name']):
            raise serializers.ValidationError('Name should Contain any shymbols')

        return data
    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''))
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
