from django.contrib import admin
from useraccount.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("contact", "address", "bank_name", )
