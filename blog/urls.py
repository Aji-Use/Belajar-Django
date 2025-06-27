from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('',  views.index, name='blog'),
    path('<str:categoryInput>/', views.category_post, name='category_post'),
    path('<str:categoryInput>/<str:slugInput>', views.detail_post, name="detail_post")
]
