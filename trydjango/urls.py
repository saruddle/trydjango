from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import pages.forms
import pages.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^resources$', app.views.resources, name='resources'),
    url(r'^products$', app.views.products, name='products'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),


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