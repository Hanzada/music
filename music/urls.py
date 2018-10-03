"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from new import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('audio/', views.index1, name='index1'),
    path('audio/create', views.Audio_create.as_view(), name='audio_create'),
    path('audio/<str:slug>/update/', views.Audio_update.as_view(), name='audio_update'),
    path('audio/<str:slug>/delete/', views.Audio_delete.as_view(), name='audio_delete'),
    path('audio/<str:slug>', views.Audio_detail.as_view(), name='audio_detail'),
    path('video/', views.index2, name='index2'),
    path('video/create/', views.Video_create.as_view(), name='video_create'),
    path('video/<str:slug>/update/', views.Video_update.as_view(), name='video_update'),
    path('video/<str:slug>/delete/', views.Video_delete.as_view(), name='video_delete'),
    path('video/<str:slug>', views.Video_detail.as_view(), name='video_detail'),
    path('gallery/', views.index3, name='index3'),
    path('authors/', views.Author_list.as_view(), name='index4'),
    path('author/<str:slug>',views.Author_detail.as_view(),name='author_detail'),
    path('genre/<str:slug>',views.Genre_detail.as_view(),name='genre_detail'),
    path('index5/', views.index5, name='index5'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)