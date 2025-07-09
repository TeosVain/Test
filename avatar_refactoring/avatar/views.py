from rest_framework import viewsets

from .models import Avatar
from avatar.serializers import AvatarWriteSerializer, AvatarReadSerializer


class AvatarHandlerViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarReadSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return AvatarWriteSerializer
        return super().get_serializer_class()