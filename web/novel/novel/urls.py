"""novel URL Configuration

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
# from django.contrib import admin
from django.urls import path
from novelweb.views import douluo, tsxk

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('novel/cover/', douluo.novel_cover),

    path("novel/douluo/", douluo.novel_douluo),
    path('novel/<int:nid>/douluo/', douluo.novel_douluo_page),

    path("novel/tsxk/", tsxk.novel_tsxk),
    path('novel/<int:nid>/tsxk/', tsxk.novel_tsxk_page),
]
