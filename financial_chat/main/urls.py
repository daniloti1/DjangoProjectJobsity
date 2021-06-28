from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *


urlpatterns = [

    path('register/', register, name='register'),
    path('login/',  auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),

    path('messages/create/', messageCreate, name='messages-create'),
    path('messages/list/', messageList, name='messages-list'),

    path('messages/create/bot/', messageCreateBOT, name='messages-create-bot'),

]
