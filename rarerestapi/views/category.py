"""View module for handling requests about game types"""
# from multiprocessing import Event
# from unicodedata import category
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from rarerestapi.models.category import Category
# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class CategoryView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        categories = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categories)
        return Response(serializer.data)
        
    # @permission_classes([AllowAny])
    def list(self, request):
        categories = Category.objects.objects.all()            
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
                

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Category
        fields = ('label')