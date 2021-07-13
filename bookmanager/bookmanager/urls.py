"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/2003/',views.index),#qianmian meiyou /
    path('',views.index_view),
    path('page/1',views.page1_view),
    path('page/<int:pg>',views.pagen_view),
    path('<int:a>/<str:b>/<int:c>',views.cal_view),
    re_path(r'^(?P<a>\d{1,2})/(?P<b>\w+)/(?P<c>\d{1,2})$',views.cal_view)
]

