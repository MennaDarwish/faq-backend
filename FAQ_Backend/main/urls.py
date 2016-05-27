from django.conf.urls import url
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^questions/$', views.QuestionList.as_view(), name="question-list"),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(),
        name="question-detail"),
    url(r'^tags/$', views.TagList.as_view(), name="tag-list"),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view(),
        name="tag-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
