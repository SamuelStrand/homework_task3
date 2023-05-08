from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django_app import views

app_name = 'django_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.list_compr, name='list_comrp'),
    path('login_f/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),

    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/detai/l', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('all_users/', views.all_users, name='all_users'),
    path('register/', views.register, name='register'),
    path('get_data_excel/', views.get_data_excel, name='get_data_excel'),
    # path('post/create', views.post_create, name='post_create'),
    # path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),
    # path('post/<int:pk>/update/', views.post_update, name='post_update'),
    # path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

]
