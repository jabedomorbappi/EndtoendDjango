
from django.contrib import admin
from django.urls import path
from .views import home,about,information


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name='home_page'),
    path('about/',about,name='about_page'),
    path('info/',information,name='info_page')
    
]
