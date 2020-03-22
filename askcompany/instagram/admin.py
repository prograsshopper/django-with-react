from django.contrib import admin
from .models import Post

# admin.site.register(Post)

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message', 'is_public', 'created_at', 'updated_at']  # pk는 id의 alias
    list_display_links = ['message']
    search_fields = ['message']
    list_filter = ['message', 'created_at', 'updated_at', 'is_public']

    def message_length(self, post):
        return len(post.message)

# admin.site.register(Post, PostAdmin)