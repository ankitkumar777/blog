from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndexView.as_view(), name = 'index'),
    path('post/<str:pk>', views.post, name = 'post')
]
