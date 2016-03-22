from rest_framework import serializers
from .models import Idea

class IdeaListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Idea
		fields = ('pk', 'name', 'votes')

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('pk', 'name', 'description', 'votes')