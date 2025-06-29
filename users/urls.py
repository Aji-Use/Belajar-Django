from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.read_data, name='administrator'),
    path('add_user/', views.add_user, name='add_user'),
    # path('administrator/', views.read_data, name='add_user')
]
