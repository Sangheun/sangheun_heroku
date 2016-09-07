from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^(?P<post_id>\d+)/$', views.delete_post, name='delete_post'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^tablet/', views.tablet_layout, name="tablet_layout"),
    url(r'^fixedbar/', views.fixed_bar, name="fixed_bar"),
    url(r'^socialmain/', views.social_main, name="social_main"),
]

