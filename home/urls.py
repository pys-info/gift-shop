from . import views
from django.urls import path

urlpatterns = [

  path('index/', views.Home.as_view()),

]
