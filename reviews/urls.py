from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_index, name='reviews_index'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
    path('create', views.review_upload, name='review_create'),   
]
