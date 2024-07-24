from django.contrib import admin
from .models import Doneer, Donee  # استيراد النماذج الخاصة بك

@admin.register(Doneer)
class DoneerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')  # الحقول التي تريد عرضها في القائمة

@admin.register(Donee)
class DoneeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')  # الحقول التي تريد عرضها في القائمة