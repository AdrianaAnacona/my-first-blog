from django.conf.urls import include, url
from . import views
	
urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="detail_post"),
	url(r'^post/new/$', views.post_new, name='post_new'),
]