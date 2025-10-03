from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('claim/<int:post_id>/', views.claim_post, name='claim_post'),
]