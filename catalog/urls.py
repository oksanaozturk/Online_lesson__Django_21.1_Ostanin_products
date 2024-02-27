from django.urls import path
from catalog.views import contacts, products_list, product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', products_list, name='products_list'),
    # path('', home_page, name='home_page'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_detail, name='product_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Другой вариант прописывания media путей
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
