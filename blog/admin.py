# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article
from .models import Author
from .models import Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author', 'Tags',)

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)