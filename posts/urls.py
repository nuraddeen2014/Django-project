from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('post/<str:pk>', views.post, name='post'),
    path('createpost', views.createpost, name='createpost'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login')


    
]

