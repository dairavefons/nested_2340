from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'product_type', 'condition', 'is_claimed', 'created_at']
    list_filter = ['condition', 'is_claimed', 'created_at', 'product_type']
    search_fields = ['title', 'description', 'author__username']
    readonly_fields = ['created_at', 'updated_at']
