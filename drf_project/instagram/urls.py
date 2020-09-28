from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개 URL을 만들어줌
# router.urls # url pattern list

urlpatterns = [
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
    # path('public/', views.PublicPostListAPIView.as_view()),
    path('', include(router.urls))
]
