from django.conf import settings
from django.db import models

# 시그널: 일종의 이벤트 핸들러
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6) # , validators=[]
