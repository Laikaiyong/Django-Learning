from django.shortcuts import render
from rest_framework import generics, parsers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import QuestionSerializer

from polls.models import Question

# Create your views here.

class QuestionViewSet(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer