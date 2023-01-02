
from django.urls import path

from home.views import HomeView, AboutView

urlpatterns = [

    path('', HomeView.as_view(), name='index'),
    path('aboutus/', AboutView.as_view(), name='aboutus'),

]
