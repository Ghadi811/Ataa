from django.contrib import admin
from .models import Doneer, Donee

@admin.register(Doneer)
class DoneerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')

@admin.register(Donee)
class DoneeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')