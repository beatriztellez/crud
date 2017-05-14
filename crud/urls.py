"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
 url(r'^cursos/', include('courses.urls', namespace='courses')),
 url(r'^admin/', admin.site.urls),
 url(r'^accounts/', include('registration.backends.default.urls')),#esta es la url de redux para poder crear modificar y logearte e no ksi ok son u buen de archivos no ma asi es amor y aun habian mas pero en el video solo utilizaban esos saz n ma
 url(r'^',include('courses.urls')),


]
