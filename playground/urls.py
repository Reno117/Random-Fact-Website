from django.urls import path
from . import views

#URLConf model
urlpatterns = [
  path('hello/', views.say_hello)
]