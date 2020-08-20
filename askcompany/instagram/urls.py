from django.urls import path, re_path, register_converter

from . import views
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram' # 향휴 reverse등을 사용할 때를 대비

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>', views.post_archive_year, name='post_archive_day'),
]