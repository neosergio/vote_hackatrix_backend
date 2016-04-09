from .models import Idea
from .serializers import IdeaSerializer, IdeaListSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET',])
def idea_list(request):
    if request.method == 'GET':
        ideas = Idea.objects.all()
        serializer = IdeaListSerializer(ideas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def idea(request, pk):
    if request.method == 'GET':
        idea = Idea.objects.get(pk=pk)
        serializer = IdeaSerializer(idea)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def results(request):
    if request.method == 'GET':
        ideas_ordered = Idea.objects.order_by('-votes')
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


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})