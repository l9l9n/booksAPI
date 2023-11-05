from django.contrib import admin
from .models import Book, UserBookRelation


@admin.register(Book)
class AdminDisplay(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
    ]


@admin.register(UserBookRelation)
class UserBookRelationAdmin(admin.ModelAdmin):
    pass


