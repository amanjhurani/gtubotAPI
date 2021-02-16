from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CircularSerializer
from .models import Circular

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['GET', 'DELETE', 'PUT'])
def get_post_list(request):
    try:
        post = Circular.objects.all()
    except Circular.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CircularSerializer(post, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        data = {
            'news': request.data.get('news'),
        }
        serializer = CircularSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)