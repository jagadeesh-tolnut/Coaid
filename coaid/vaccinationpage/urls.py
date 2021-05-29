from django.urls import path
from . import views

app_name = 'vaccinationpage'

urlpatterns = [
    path('', views.vacpage, name='vaccinationpage')
]