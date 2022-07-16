"""View module for handling requests about game types"""
# from multiprocessing import Event
# from unicodedata import category
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from rarerestapi.models.tag import Tag
# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class TagView(ViewSet):
    """Level up game types view"""
    
       
    # @permission_classes([AllowAny])
    def list(self, request):
        tags = Tag.objects.all()            
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Tag
        fields = ('id','label')
