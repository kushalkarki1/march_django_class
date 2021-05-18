from django.shortcuts import render, reverse, get_object_or_404
from product.forms import ProductCreateForm
from product.models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def create_product(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse("product:list_product"))
    return render(request, "form.html", {"form": form})

class CreateProduct(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("product:list_product")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Product"
        return context

@login_required
def list_product(request):
    product_list = Product.objects.filter(user=request.user)
    return render(request, "product_list.html", {"products": product_list, "title": "Product List"})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ProductCreateForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("product:list_product"))
    return render(request, "form.html", {"form": form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse("product:list_product"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:login"))