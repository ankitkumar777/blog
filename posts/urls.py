from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('contact/', views.ContactView.as_view(), name = 'contact'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('signup/', views.user_signup, name = 'signup'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('add/', views.add_post, name = 'addpost'),
    path('update/<int:pk>', views.update_post, name = 'updatepost'),
    path('delete/<int:pk>', views.delete_post, name = 'deletepost'),
    path('post/<str:pk>', views.post, name = 'post'),
    
]
