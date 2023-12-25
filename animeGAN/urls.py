"""animeGAN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app01.views import account, style_conversion
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # path("admin/", admin.site.urls),

    # 配置 URL 映射，以便在访问 "media/" 开头的 URL 时，能够提供静态文件的访问服务
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 首页
    path("homepage/", style_conversion.homepage),
    # 风格转换
    path("upload/", style_conversion.upload),
    # 展示页
    path("exhibition1/", style_conversion.exhibition1),
    path("exhibition2/",style_conversion.exhibition2),

    # 注册登录
    path("login/", account.login),
    path("signup/", account.signup),
    path("logout/", account.logout),
    path("forget/", account.forget),

]
