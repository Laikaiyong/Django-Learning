from django.urls import path

from .views import (
    product_profile_view, 
    product_create_view,
    product_delete_view,
    product_update_view,
    product_list_view
)

app_name = 'product'
urlpatterns = [
    path('', product_list_view, name="product-list"),
    path('<int:product_id>/', product_profile_view, name="product-profile"),
    path('<int:product_id>/delete/', product_delete_view, name="product-delete"),
    path('<int:product_id>/update/', product_update_view, name="product-update"),
    path('create/', product_create_view, name="product-create"),
]
