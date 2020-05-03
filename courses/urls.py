from django.urls import path, re_path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='courses'),
    re_path(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail, name='step'),
    re_path(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
