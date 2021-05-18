from django.urls import path
from product.views import create_product, list_product, edit_product, delete_product, CreateProduct, logout_view

app_name = "product"

urlpatterns = [
    path("add-product/", CreateProduct.as_view(), name="add_product"),
    path("list-product/", list_product, name="list_product"),
    path("edit-product/<int:product_id>/", edit_product, name="edit_product"),
    path("delete-product/<int:product_id>/", delete_product, name="delete_product"),
    path("logout/", logout_view, name="logout"),
]
