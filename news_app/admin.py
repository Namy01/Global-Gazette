from django.contrib import admin
from .models import Category, Comment, Contact, Post, Tag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Contact)
