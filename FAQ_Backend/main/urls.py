from django.conf.urls import url
from main import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token


router = routers.SimpleRouter()
router.register("questions/search", views.AutocompleteSearchViewSet,
                base_name="questions-search")


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^questions/$', views.QuestionList.as_view(), name="question-list"),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(),
        name="question-detail"),
    url(r'^tags/$', views.TagList.as_view(), name="tag-list"),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view(),
        name="tag-detail"),
    url(r'^answers/$', views.AnswerList.as_view(), name="answer-list"),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerDetail.as_view(),
        name="answer-detail"),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^restricted/$', views.RestrictedView.as_view()),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
