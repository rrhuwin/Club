from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^register', views.index),
    # url(r'details/all', views.details,name='detail'),
    url(r'details/a', views.adetails, name='detaila'),
    url(r'details/h', views.hdetails, name='detailh'),
    url(r'details/s', views.sdetails, name='details'),
    url(r'check/', views.check, name='check'),
    url(r'cancelc', views.cancelc, name='cancelc'),
    url(r'canceld', views.canceld, name='canceld'),
    url(r'sc/(?P<id>\d+)', views.QuestionCollectionView.as_view(), name='sc'),
    url(r'dz/(?P<id>\d+)', views.QuestionlikeView.as_view(), name='dz'),

]
