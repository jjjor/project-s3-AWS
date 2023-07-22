from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


"""faz o registro dos planos"""


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'imagem')
