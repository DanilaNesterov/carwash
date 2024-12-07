from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_service, name='book_service'),
    path('schedule/', views.schedule, name='schedule'),
]