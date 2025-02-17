
from django.contrib import admin
from django.urls import path,include
from .views import home,about,information

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    
    #connect LearnModels app
    path('learnmodels/', include('LearnModels.urls')),
    path("learnforms/",include("LearnForms.urls")),
    path("learnformmodels/",include("LearnFormModels.urls")),
    path("tution/",include("tution.urls")),
    
    
    
    path('',home,name='home_page'),
    path('about/',about,name='about_page'),
    path('info/',information,name='info_page'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


