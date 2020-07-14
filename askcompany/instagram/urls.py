from django.urls import path, re_path, register_converter

from . import views


class YearConverter:
    # 자주 쓰는 패턴이 있다면 이렇게 커스텀 컨버터를 활용하는 것도 괜찮다.
    regex = r"20\d{2}"
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'year')

app_name = 'instagram' # 향휴 reverse등을 사용할 때를 대비

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    path('archives/<year:year>/', views.archives_year),
]