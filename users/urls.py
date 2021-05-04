from django.urls import path
from . import views

app_name = 'user_namespace'

urlpatterns = [
    path('', views.profile, name="user_profile"),
    
 

]