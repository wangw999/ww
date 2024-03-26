"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from myapp import views, ajaxTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myappInit/', views.hello_world, name='hello_world'),
    path('ajax111/', ajaxTest.my_ajax_view, name='my_ajax_view'),
    path('downLoad/', ajaxTest.downloadFile, name='downloadFile'),
    path('upload/', ajaxTest.upload_file_view, name='upload_file_view'),
]

# http://127.0.0.1:8000/myappInit/
# djiango 4.1.13