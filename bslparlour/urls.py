from django.conf.urls import url, include

from bslparlour import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^source_videos/$', views.SourceVideoList.as_view()),
    url(r'^not_source_videos/$', views.NotSourceVideoList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    # url(r'^(?P<gloss_str>[A-Z-]+)/$', views.gloss, name='gloss'),
    # url(r'^(?P<word_str>[a-z-]+)/$', views.english, name='english'),
]
