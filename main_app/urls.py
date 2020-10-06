from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('api/', views.api, name='api'),
  path('pets/', views.pets_index, name='pets_index'),
  path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
  path('pets/<int:pet_id>/delete/', views.pets_delete, name='pets_delete'),
  path('pets/<int:pet_id>/edit/', views.pets_edit, name='pets_edit'),
  path('pets/<int:pet_id>/add_vaccine/', views.add_vaccine, name='add_vaccine'),
]
