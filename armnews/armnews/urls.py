
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('news.urls')),
    url(r'^accounts/login/$', login, name='accounts/login/'),
    url(r'^accounts/logout/$', logout, name='accounts/logout/', kwargs={'next_page': '/'}),
]
