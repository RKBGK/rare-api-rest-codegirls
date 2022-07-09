from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from rarerestapi.models.rareuser import RareUser

class RareUserView(ViewSet):
    """User view"""
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        users = RareUser.objects.get(pk=pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)
    # @permission_classes([AllowAny])
    def list(self, request):
        users = RareUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    class Meta:
        model = RareUser
        fields = ('user', 'bio', 'image_url', 'created_on', 'active')
        depth = 1


