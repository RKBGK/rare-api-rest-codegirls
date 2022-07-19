"""View module for handling requests about game types"""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action

from rarerestapi.models import Post, Reaction, RareUser, Tag, Category, Comment, RareUser, TagPost
from rarerestapi.models.subscription import Subscription

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
        rareuser = RareUser.objects.get(user=request.auth.user)
        serializer = CreatePostSerializer(data=request.data)
        print("*" * 100)
        print(CreatePostSerializer(data=request.data))        
        serializer.is_valid(raise_exception=True)
        serializer.save(user=rareuser)
        postid = serializer.data['id']
        post= Post.objects.get(pk=postid)
        tags =  request.data['tags']
        # *tags is spread in python
        post.tags.add(*tags)
        
        # for tag in request.data['tags']:
        #     print("*" * 100)
        #     print(tag) 
        #     print(serializer.data['id']) 
        #     vtag = Tag.objects.get(pk=tag)
        #     post= Post.objects.get(pk=postid)
        #     post.tags.add(tag)
            # newtag = CreateTagSerializer(tag_id=tag, post=postid)
            # newtag.save()
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # http://localhost:8000/posts/2/randomuserpost
    
    @action(methods=['get'], detail=True)
    def randomuserpost(self, request,pk):
        user = RareUser.objects.get(user=pk)
        posts = Post.objects.all().filter(user_id=user)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def subscribed(self, request):
        """Get request to display posts of authors logged-in user is subscribed to """
        posts = Post.objects.all()
        subs = Subscription.objects.all()
        user = RareUser.objects.get(user=request.auth.user)
        print('*************************')
        print(request.auth.user)
        user_subs = subs.filter(follower=user)
        if len(user_subs) > 0:
            for user_sub in user_subs:
                posts = posts.filter(user=user_sub.author)
        else:
            posts=[]
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
        
        # django relationship set
        # tags =  post.tags.objects.all()
        # post.tags.delete(*tags)
        newtags =  request.data['tags']
        post.tags.set(newtags)
        return Response(None, status=status.HTTP_204_NO_CONTENT)   

    
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
    def untagpost(self, request):
        """Post request for a user to sign up for an event"""
        # instatiate objects
        
        tag_id = request.data["tag"]
        post_id = request.data["post"]
        post = Post.objects.get(pk=post_id)
        tag = Tag.objects.get(pk=tag_id)
        post.tags.remove(tag)
        return Response({'message': 'Tagged added'}, status=status.HTTP_201_CREATED)    
      
class  PostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date',
          'image_url', 'content', 'approved','category','user','tags','tagged')
        depth = 2
 
class  CreatePostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date',
          'image_url', 'content', 'approved','category')
        
# class  CreateTagSerializer(serializers.ModelSerializer):
#     """JSON serializer for game types
#     """
    
#     class Meta:
#         model = TagPost
#         fields = ('id', 'post', 'tag')
        
        