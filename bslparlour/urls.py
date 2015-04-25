from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<gloss_str>[A-Z-]+)/$', views.gloss, name='gloss'),
    # url(r'^(?P<word_str>[a-z-]+)/$', views.english, name='english'),
]
