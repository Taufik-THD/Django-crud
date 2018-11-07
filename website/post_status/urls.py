from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('post/', views.post, name='post'),
    path('update/<int:id>/', views.edit_status, name='edit_status'),
    path('delete/<int:id>/', views.remove, name='remove_status'),
    path('comment/<int:id>/', views.add_comment, name='add_comment')

]
