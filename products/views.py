from django.views.generic import DetailView, TemplateView, ListView

from products.models import Product, Category


# Create your views here.
class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    model = Product


class NavbarPartialView(TemplateView):
    template_name = 'includes/navbar.html'

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductsListView(ListView):
    template_name = 'products/products_list.html'
    queryset = Product.objects.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        request = self.request
        search_query = request.GET.get('q')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        categories = request.GET.getlist('category')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        queryset = Product.objects.all()

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()

        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()

        if categories:
            queryset = queryset.filter(category__slug__in=categories).distinct()

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        self.object_list = queryset

        context = super().get_context_data(**kwargs)
        context['selected_colors'] = colors
        context['selected_sizes'] = sizes
        context['selected_categories'] = categories
        context['categories'] = Category.objects.all()
        context['min_price'] = min_price
        context['max_price'] = max_price
        return context
