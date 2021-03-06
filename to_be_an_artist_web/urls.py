"""to_be_an_artist_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from backend import views as back_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    path(r'api/',back_view.index,name='index'),
    path(r'api/gen/',back_view.gen_f_poetry,name='gen'),
    path(r'api/logon/',back_view.logon,name='logon'),
    path(r'api/token/',back_view.token,name='token'),
    path(r'api/login/',back_view.login,name='login'),
    path(r'api/user/',back_view.user,name='user'),
    path(r'api/save/',back_view.save,name='save'),
    path(r'api/quit/',back_view.quit,name='quit'),
    path(r'api/queryAll/',back_view.queryAll,name='queryAll'),
    path(r'api/isave/',back_view.isave,name='isave'),
    path(r'api/delrecord/',back_view.delrecord,name='delrecord'),
]
