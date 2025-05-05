from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
# Create your views here.

class HomePage(ListView):
    model = Book
    ordering = ("-created_at")
    context_object_name = "books"
    template_name = "home/index.html"