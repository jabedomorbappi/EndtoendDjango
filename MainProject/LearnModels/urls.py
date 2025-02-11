from django.urls import path
from . import views  # Import views

app_name = 'LearnModels'  # Namespace for the app

urlpatterns = [
    path('learn/', views.showLearnmodels, name='showLearnmodels'), 
    path('second/', views.showSecond, name='showSecond'),
    # URL changed
]
