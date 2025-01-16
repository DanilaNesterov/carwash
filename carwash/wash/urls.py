from django.urls import path
from . import views


handler404 = 'wash.views.handler_404'
handler500 = 'wash.views.handler_500'
handler403 = 'wash.views.handler_403'


urlpatterns = [
    path('', views.book_service, name='book_service'),
    path('schedule/', views.schedule, name='schedule'),
]

