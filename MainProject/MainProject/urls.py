
from django.contrib import admin
from django.urls import path,include
from .views import home,about,information


urlpatterns = [
    path("admin/", admin.site.urls),
    
    #connect LearnModels app
    path('learnmodels/', include('LearnModels.urls')),
    path("learnforms/",include("LearnForms.urls")),
    
    
    path('',home,name='home_page'),
    path('about/',about,name='about_page'),
    path('info/',information,name='info_page'),
    
]
