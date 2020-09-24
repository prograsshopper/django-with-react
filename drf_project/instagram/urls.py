from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개 URL을 만들어줌
# router.urls # url pattern list

urlpatterns = [
    path('', include(router.urls))
]
