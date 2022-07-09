"""View module for handling requests about game types"""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action

from rarerestapi.models import Post, Reaction, RareUser, Tag, Category, Comment, RareUser

class PostView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        posts = Post.objects.get(pk=pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)    
    def currentUser(self, request):
        user = RareUser.objects.get(user=request.auth.user)
        posts = Post.objects.all().filter(user_id=user)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)
    
    def create(self, request):
        post = Post.objects.get(pk=request.data["post"])
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # http://localhost:8000/posts/2/randomuserpost
    
    @action(methods=['get'], detail=True)
    def randomUserPost(self, request,pk):
        user = RareUser.objects.get(user=pk)
        posts = Post.objects.all().filter(user_id=user)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)
    

    def destroy(self, request, pk):
        event = Post.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        post = Post.objects.get(pk=pk) 
        serializer = CreatePostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    
        # serializer = CategorySerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
    
    @action(methods=['post'], detail=False)
    def tagpost(self, request):
        """Post request for a user to sign up for an event"""
        # instatiate objects
        
        tag_id = request.data["tag"]
        post_id = request.data["post"]
        post = Post.objects.get(pk=post_id)
        tag = Tag.objects.get(pk=tag_id)
        post.tags.add(tag)
        return Response({'message': 'Tagged added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=False)
    def tagpost(self, request):
        """Post request for a user to sign up for an event"""
        # instatiate objects
        
        tag_id = request.data["tag"]
        post_id = request.data["post"]
        post = Post.objects.get(pk=post_id)
        tag = Tag.objects.get(pk=tag_id)
        post.tags.remove(tag)
        return Response({'message': 'Tagged added'}, status=status.HTTP_201_CREATED)
    
    # @action(methods=['delete'], detail=True)
    # def untag(self, request, pk):
    #     """Post request for a user to sign up for an event"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     event = Event.objects.get(pk=pk)
    #     event.attendees.remove(gamer)
    #     return Response({'message': 'Gamer removed'}, status=status.HTTP_201_CREATED)     
    
    
class  PostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date',
          'image_url', 'content', 'approved','category','user','tags')
        depth = 2
 
class  CreatePostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date',
          'image_url', 'content', 'approved','category')
        