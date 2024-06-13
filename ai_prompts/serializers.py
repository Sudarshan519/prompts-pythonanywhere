from rest_framework import serializers
from .models import Prompt, PromptDetail

class PromptDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptDetail
        fields = ['id', 'element']
        fields = '__all__'

class PromptSerializer(serializers.ModelSerializer):
    details = PromptDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Prompt
        fields = ['id', 'content', 'category', 'details']
