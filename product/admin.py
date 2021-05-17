from django.contrib import admin
from product.models import Weight

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ("weight_range", "price", )
