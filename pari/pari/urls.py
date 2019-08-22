"""pari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,handler404,handler500
from pari import views
from django.urls import include,path
from app_pari import views as user_views
#from django.contrib.auth import views as auth_views

handler404 = 'pari.views.handler404'
handler500 = 'pari.views.handler500'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.home,name='home'),
    path('score/',views.score,name='score'),
    path('resultat/',views.resultat,name='resultat'),
    path('admin/', admin.site.urls),
    path('app_pari/',include('app_pari.urls')), #url application
    path('register/',user_views.register,name='register')
]
