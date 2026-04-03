from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.get_records),
    path('records/create/', views.create_record),
    path('records/<int:pk>/', views.update_record),
    path('records/delete/<int:pk>/', views.delete_record),

    path('dashboard/', views.dashboard),

    path('users/', views.get_users),
    path('users/<int:pk>/', views.update_user),
]