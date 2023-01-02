from django.views.generic import TemplateView
from oscar.core.loading import get_model

from home.models import Slider

Product = get_model('catalogue', 'product')
Category = get_model('catalogue', 'category')


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['products'] = Product.objects.all()
        context['categorys'] = Category.objects.all()

        return context


class AboutView(TemplateView):
    template_name = 'home/aboutus.html'
