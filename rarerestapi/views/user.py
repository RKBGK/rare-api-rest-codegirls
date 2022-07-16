from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from rarerestapi.models import RareUser, Post
from rest_framework.decorators import action

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
    
    
    @action(methods=['get'], detail=True)
    def userpost(self, request,pk):
        print("*****************************")
        print(pk)
        posts = Post.objects.all().filter(user_id=pk)
        serializer = UserPostSerializer(posts, many=True)
        
        return Response(serializer.data)

    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    # https://github.com/encode/django-rest-framework/issues/5937
    print('*' * 100)
    print(first_name)
    class Meta:
        model = RareUser

        fields = ('user', 'bio', 'image_url', 'created_on', 'active','first_name','last_name')
        #depth = 1
        
class UserPostSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    user = UserSerializer(many=False)
    class Meta:
        model = Post
        fields = ('title', 'publication_date','image_url', 'content', 'approved','category','user')