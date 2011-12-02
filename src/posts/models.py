from django.db import models
from datetime import datetime

class Post(models.Model):
    prepopulated_fields = {"slug": ("title",)}

    title_help = "The title of the post."
    title = models.CharField(max_length=256, help_text=title_help)
    
    slug_help = "The slug field string for the post."
    slug = models.SlugField(help_text=slug_help)
    
    body_help = "The main text of the post."
    body = models.TextField(help_text=body_help)
    
    publish_help = "Flags whether the post is to be visable on the blog."
    published = models.BooleanField(default=True)
    
    date_created_help = "Auto populated field for when a post was created."
    date_created = models.DateTimeField(auto_now_add=True, help_text=date_created_help)
    
    last_updated_help = "Auto populated field for when the post was last updated."
    last_updated = models.DateTimeField(auto_now=True, help_text=last_updated_help)