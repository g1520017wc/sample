"""hodicproject URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlcomp = '-HODIC管理者用URL-アドミンページ閲覧用-hodicadmin-/'

urlpatterns = [
    path('admin/' + urlcomp, admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('', include("apps.hodic.urls", namespace='hodic')),
    path('prize/', include("apps.prize.urls")),
    path('meeting/', include("apps.meeting.urls")),    
    path('information/', include("apps.information.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)