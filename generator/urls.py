from generator.views import *
from django.urls import path

urlpatterns = [
    path('avatar/', Avatar.as_view()),
]
