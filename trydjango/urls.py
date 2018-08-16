from datetime import datetime
from django.conf.urls import url
from pages.views import home, blog, about, products, resources, contact

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^blog$', blog, name='blog'),
    url(r'^resources$', resources, name='resources'),
    url(r'^products$', products, name='products'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about$', about, name='about'),
    ]


#"""trydjango URL Configuration

#The `urlpatterns` list routes URLs to views. For more information please see:
#    https://docs.djangoproject.com/en/2.0/topics/http/urls/
#Examples:
#Function views
#    1. Add an import:  from my_app import views
#    2. Add a URL to urlpatterns:  path('', views.home, name='home')
#Class-based views
#    1. Add an import:  from other_app.views import Home
#    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
#Including another URLconf
#    1. Import the include() function: from django.urls import include, path
#    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
#"""
#from django.contrib import admin
#from django.urls import path
#from pages.views import home_view

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', home_view, name = 'home_view' ) ]