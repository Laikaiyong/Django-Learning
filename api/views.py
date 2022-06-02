from django.shortcuts import render
from rest_framework import generics, parsers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import QuestionSerializer, ChoiceSerializer

from polls.models import Question, Choice

# Create your views here.

class QuestionViewSet(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer