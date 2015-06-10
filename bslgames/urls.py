from django.conf.urls import url, include

from bslgames import views

urlpatterns = [
    url(r'^namethatsign/$', views.name_that_sign, name='name_that_sign'),
    url(r'^$', views.index, name='index'),
]
