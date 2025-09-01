from django.views.generic import TemplateView

from products.models import Category, Product


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context

