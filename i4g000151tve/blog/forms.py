from dataclasses import field
from django import forms
from .models import PostApp

class PostAppForm(forms):
    class Meta:
        model = PostApp
        field =[
            "title",
            "description",
            "author",
            "created_date",
            "published_date"
        ]