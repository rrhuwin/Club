from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^register', views.index),
    url(r'^login/$', views.register, name='register'),
    url(r'^login1/$', views.login, name='login1'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^change/$', views.Change.as_view(), name='change'),
    url(r'^newpass/(\w+)/$', views.PasswordReset.as_view(), name="password_reset"),
    url(r'^users/$', views.ProfileView.as_view(), name='users'),

    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),

]
