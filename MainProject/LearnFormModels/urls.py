from django.urls import path

from .views import studentform

app_name = 'LearnFormModels'  # Namespace for the app

urlpatterns = [
    path('formmodels/',studentform , name='learnformmodels_url'), 
   
]
    # URL changed


