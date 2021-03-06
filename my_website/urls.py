"""my_website URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from Barghash.views import *

app_name = 'my_website'

urlpatterns = [
    path('admin/', admin.site.urls, name="Admin"),
    path('', Home.as_view(), name='Home'),
    path('collection/', Collection.as_view(), name='Collection'),
    path('test/', Test.as_view(), name='test'),
    path('about/', About.as_view(), name='About'),
    path('services/', Services.as_view(), name='Services'),
    path('blog/', Blog.as_view(), name='Blog'),
    path('blog/<str:category>/', CategoryBlog.as_view(), name='CategoryBlog'),
    path('blogs/search/', SearchResults.as_view(), name='search_results'),
    path('post/', BlogPost.as_view(), name='BlogPost'),
    path('contact/', Contact.as_view(), name='Contact'),
    path('Message-Read/', MessageRead.as_view(), name='Message-Read'),
    path('Upload-collection/', UploadCollection.as_view(), name='Upload-collection'),
    path('api/Add-Category/<str:category>/', AddCategory.as_view(), name='Add-Category'),
    path('api/send-Message/', Message.as_view(), name='Message'),
    path('api/archive/', Archive.as_view(), name='archive'),
    path('api-post/delete/<int:id>', DeletePost.as_view(), name='delete-post'),
    path('api/sync-instagram/', SyncInstagram.as_view(), name='sync-instagram'),
    path('insta/', TemplateView.as_view(template_name='index.html', extra_context={
        "instagram_profile_name": "barghash.photography"
    })),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
