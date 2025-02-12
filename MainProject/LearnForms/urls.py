from django.urls import path
from . import views  # Import views

app_name = 'LearnForms'  # Namespace for the app

urlpatterns = [
    path('contact/', views.contactview, name='contactforms'), 
    path('forms/', views.anothercontactview, name='anothercontactforms'),  # Add this line
    
    ]
    # URL changed


