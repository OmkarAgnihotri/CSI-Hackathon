from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='CSI-home'),
    path('teacher/',views.teacher,name='CSI-teacher'),
    path('transcripts/',views.speech_to_text,name='CSI-speech_to_text')
]