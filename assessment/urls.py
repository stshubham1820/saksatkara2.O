from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',AssessmentCreateView.as_view(),name='assessment_create'),
    path('<int:pk>/code/',AssessmentCodeView.as_view(),name='assessment_code_create'),
    path('<int:pk>/check/',AssessmentCheckView.as_view(),name='assessment_check'),
    path('<int:pk>/skill/',AssessmentSkillView.as_view(),name='assessment_skill'),
    path('<int:pk>/question/',QuestionCreateView.as_view(),name='question_create'),
    path('<int:pk>/question/<int:id>/',QuestionReadView.as_view(),name='question_read'),

]