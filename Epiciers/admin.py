from django.contrib import admin
from .models import Client
from .models import Produit
# Register your models here.
admin.site.register(Client)
admin.site.register(Produit)