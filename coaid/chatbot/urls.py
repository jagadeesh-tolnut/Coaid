from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chat, name='chatbot'),
]