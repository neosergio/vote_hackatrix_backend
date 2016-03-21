from .models import Idea
from .serializers import IdeaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET',])
def idea_list(request):
    if request.method == 'GET':
        ideas = Idea.objects.all()
        serializer = IdeaSerializer(ideas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def results(request):
    if request.method == 'GET':
        ideas_ordered = Idea.objects.order_by('-votes')
        serializer = IdeaSerializer(ideas_ordered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST',])
def vote(request):
    if request.method == 'POST':
        idea = Idea.objects.get(pk=request.data)
        idea.votes += 1
        idea.save()
        serializer = IdeaSerializer(idea)
        return Response(serializer.data, status=status.HTTP_200_OK)

