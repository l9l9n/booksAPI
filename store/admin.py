from django.contrib import admin
from .models import Book


@admin.register(Book)
class AdminDisplay(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
    ]

