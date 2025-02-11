from django.urls import path
from . import views  # Import views
from .views import student_registration,success_page
app_name = 'LearnModels'  # Namespace for the app

urlpatterns = [
    path('learn/', views.showLearnmodels, name='showLearnmodels'), 
    path('second/', views.showSecond, name='showSecond'),
    path('register/', views.student_registration, name='student_registration'),
    path('success/', success_page, name='success_page'),  # Add this line
]
    # URL changed


