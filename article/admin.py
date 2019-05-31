from django.contrib import admin
from .models import Article,Comment

# Register your models here.
admin.site.register(Comment)
#decoratorla ModelAdmin istifade eledik, ve Meta ile Article=model eledik
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display= ["title","author","created_data"]
    list_display_links=["title","author"]
    search_fields=["title"]
    list_filter=["created_data"]
    class Meta:
        model=Article
