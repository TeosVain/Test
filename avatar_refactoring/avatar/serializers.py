from rest_framework import serializers

from avatar.models import Avatar
from avatar_refactoring.s3_storage import generate_presigned_url


class AvatarWriteSerializer(serializers.ModelSerializer):
    '''Serializer for creating or updating an Avatar instance.'''

    class Meta:
        model = Avatar
        fields = ['id', 'image', 'name']
    

class AvatarReadSerializer(serializers.ModelSerializer):
    '''Serializer for reading Avatar instance data, including a presigned URL for the image.'''
    
    image = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        fields = ['id', 'image', 'name']

    def get_image(self, obj):
        if obj.image:
            return generate_presigned_url(obj.image.name)
        return None
