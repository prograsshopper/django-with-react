from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# admin.site.register(Post)

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo_tag', 'message', 'is_public', 'created_at', 'updated_at']  # pk는 id의 alias
    list_display_links = ['message']
    search_fields = ['message']
    list_filter = ['message', 'created_at', 'updated_at', 'is_public']

    def message_length(self, post):
        return len(post.message)
    
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url} style="width: 72px;" />"')
        return None

# admin.site.register(Post, PostAdmin)

@admin.register
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
