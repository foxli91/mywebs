"""mywebs URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from user import views as user_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userinfo/', user_view.user_info),
    url(r'^user_list/', user_view.user_list),
    url(r'home/', user_view.home),
    url(r'no_auth/', user_view.no_auth_redirect),
    url(r'^login/', user_view.login),
    url(r'^find_users/', user_view.find_users)
]
