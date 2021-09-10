from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'telefone')



admin.site.register(Client, ClientAdmin)