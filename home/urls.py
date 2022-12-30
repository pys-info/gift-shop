from . import views
from django.urls import path

urlpatterns = [

    path('', views.HomeView.as_view(), name='index'),
    path('aboutus/', views.AboutView.as_view(), name='aboutus'),

]
