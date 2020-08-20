from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Custom object id : ({self.id})"
    
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])
    
    class Meta:
        ordering = ['-id']
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE)
    # 그냥 Post 라고 해도 되고 'POST'라 하면 이 앱에서 찾고 타 입할거면 앱명 지정 가능
    # post_id 라는 애가 생김
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)    
