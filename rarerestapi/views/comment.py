"""View module for handling requests about comments"""

from dataclasses import fields
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rarerestapi.models import Comment

class CommentView(ViewSet):
    
    def retrieve(self, request, pk):
        comments = Comment.objects.get(pk=pk)
        serialzier = CommentSerializer(comments)
        return Response(serialzier.data)
    
    def list(self, request):
        comments = Comment.objects.all()
        serialzer = CommentSerializer(comments, many=True)
        return Response(serialzer.data)
    
    def create(self, request):
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)   
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post','author','content','created_on')
        
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post','author','content','created_on')