from django.views.generic import TemplateView
from .models import Slider


class HomeView(TemplateView):
    template_name = 'home/home.html'
    extra_context = {'slider': Slider.objects.all()}


class AboutView(TemplateView):
    template_name = 'home/aboutus.html'
