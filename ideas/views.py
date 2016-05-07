from .models import Idea
from .serializers import IdeaSerializer, IdeaListSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET',])
def idea_list(request):
    if request.method == 'GET':
        ideas = Idea.objects.all().filter(is_active=True)
        serializer = IdeaListSerializer(ideas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def idea(request, pk):
    if request.method == 'GET':
        idea = Idea.objects.get(pk=pk)
        serializer = IdeaSerializer(idea)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def results(request):
    if request.method == 'GET':
        ideas_ordered = Idea.objects.order_by('-votes').filter(is_active=True)
        serializer = IdeaListSerializer(ideas_ordered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST',])
def vote(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(pk=pk)
        idea.votes += 1
        idea.save()
        serializer = IdeaSerializer(idea)
        return Response(serializer.data, status=status.HTTP_200_OK)

