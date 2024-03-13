from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


# Заменяем FBV на CBV
# def products_list(request):
#     """Вывод страницу со всеми продуктами"""
#     products = Product.objects.all()
#     context = {
#         'object_list': products
#     }
#     return render(request, 'catalog/product_list.html', context)
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'category', 'description', 'price', 'preview')
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'preview')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')

# Заменяем FBV на CBV
# def product_detail(request, pk):
#     """Вывод страницу с одним продуктом по pk"""
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product
#     }
#     return render(request, 'catalog/product_detail.html', context)

# Заменили выведелие главной страницы на products_list
# def home_page(request):
#     products = Product.objects.all()
#     context = {
#         'object_list': products
#     }
#     return render(request, 'catalog/home_page.html', context)
#     # return render(request, 'catalog/home_page.html')
