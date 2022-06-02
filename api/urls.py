from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('question_list/', views.QuestionViewSet.as_view(), name='question_list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)