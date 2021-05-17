from django import forms
from product.models import Product

# class ProductCreateForm(forms.Form):
#     name = forms.CharField()
#     price = forms.CharField()
#     customer_name = forms.CharField()

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("status", "remarks", "user", )