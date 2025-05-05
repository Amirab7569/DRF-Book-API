from django.contrib import admin
from .models import Book, CustomUser
# Register your models here.



@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ["email", "is_staff", "date_joined"]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["author","title","is_published","created_at","updated_at"]
