from models import *
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'date_created', 'published']
    list_filter = ('published',)
    list_per_page = 20
    ordering = ['title', 'date_created', 'published']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    
admin.site.register(Post, PostAdmin)