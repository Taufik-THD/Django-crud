from django.urls import include, path

from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    
]