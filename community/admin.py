from django.contrib import admin
from .models import Article, Comment
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)




admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)