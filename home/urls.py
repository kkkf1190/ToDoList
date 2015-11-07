"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^$','home.views.home_page',name='home'),
                       url(r'^list/add','home.views.add_lists',name='addlist'),
                       url(r'^list/delete','home.views.delete_lists',name='addlist'),
                       url(r'^list/(.+)/add','home.views.add_list',name='addlist'),
                       url(r'^list/(.+)/updata','home.views.updata_list',name='addlist'),
                       url(r'^list/(.+)/delete','home.views.delete_list',name='addlist'),
                       url(r'^list/(.+)/', 'home.views.list', name='listdetile'),
                       url(r'^list/','home.views.lists',name='lists'),


                       )
