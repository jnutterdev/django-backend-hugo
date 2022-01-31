from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MyModel, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(MyModel, MarkdownxModelAdmin)