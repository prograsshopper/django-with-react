from django.db import models


class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Custo object id : ({self.id})"
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"
