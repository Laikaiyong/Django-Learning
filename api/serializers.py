from rest_framework import serializers, status
from rest_framework.response import Response

from polls.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'