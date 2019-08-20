"""recover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib.staticfiles.urls import
# from apps.count import views
from apps.content import views
from recover import settings
from django.contrib.staticfiles.views import static

# import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index', views.index, name='index'),
    url(r'^music', views.music, name='music'),
    url(r'^show', views.Show.as_view(), name='video'),
    url(r'^bsi/$', views.bsi, name='bsi'),
    url(r'^bsi/(?P<p_id>\d+)$', views.bsi_cont, name='bsi_cont'),
    url(r'^ancient/$', views.ancient, name='ancient'),
    url(r'^ancient/(?P<p_id>\d+)$', views.ancient_cont, name='ancient_cont'),
    url(r'^news/(?P<tp>[a-z]+)/(?P<page>\d+)', views.news, name='news'),
    url(r'^contents/(?P<tpa>[a-z]+)/(?P<pn>\d+)', views.contents, name='contents'),


    url(r'^count/', include('apps.count.urls', namespace='count')),
    url(r'^questions/', include('apps.questions.urls', namespace='questions')),
    url(r'^apis/', include('apps.apis.urls', namespace='apis')),

    # 404定制
    # url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static')
]

# handler404=views.my404
#
