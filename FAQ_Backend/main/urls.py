from django.conf.urls import url
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^questions/$', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
