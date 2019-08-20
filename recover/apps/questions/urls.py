from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^register', views.index),
    url(r'details/all', views.details,name='detail'),
    url(r'details/h', views.hdetails, name='detailh'),
    url(r'details/s', views.sdetails, name='details'),
    url(r'check/', views.check, name='check'),
    url(r'dz/(?P<id>\d+)', views.QuestionCollectionView.as_view(), name='dz'),
    url(r'sc/(?P<id>\d+)', views.QuestionlikeView.as_view(), name='sc'),

]
