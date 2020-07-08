import os
# python manage.py shell

os.environ['DJANGO_SETTINGS_MODULE'] = 'askcompany.settings'
# os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true' 
# Django 3.0부터는 비동기를 지원하기 때문에 주피터 사용시 이 부분 필요

import django

django.setup()

from instagram.models import Post
posts = Post.objects.all() 