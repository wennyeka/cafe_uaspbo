from django.contrib import admin
from .models import *

class koordinatadmin(admin.ModelAdmin):
    list_display = ['nama_cafe', 'koordinat']
    search_fields = ['nama_cafe']
    list_per_page = 5

class cafeadmin(admin.ModelAdmin):
    list_display = ['nama_cafe', 'alamat', 'no_tlp']
    search_fields = ['nama_cafe']
    list_per_page = 5


admin.site.register(Koordinat, koordinatadmin)
admin.site.register(Cafe, cafeadmin)

# Register your models here.