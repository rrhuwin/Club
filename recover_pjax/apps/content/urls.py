from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^show', views.show, name='show'),
    url(r'^bsi/$', views.bsi, name='bsi'),
    url(r'^music$', views.music, name='music'),
    url(r'^music2$', views.music2, name='music2'),
    url(r'^bsi/(?P<p_id>\d+)', views.bsi_cont, name='bsi_cont'),
    url(r'^ancient$', views.ancient, name='ancient'),
    url(r'^ancient/(?P<p_id>\d+)', views.ancient_cont, name='ancient_cont'),

    url(r'^news/(?P<tp>[a-z]+)/(?P<page>\d+)', views.news, name='news'),
    url(r'^contents/(?P<tpa>[a-z]+)/(?P<pn>\d+)', views.contents, name='contents'),

]
