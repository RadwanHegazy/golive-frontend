from django.urls import path
from .views.auth import login, logout, register
from .views.room import get, create, delete

urlpatterns = [
    # authentication 
    path('account/login/',login.LoginView,name='login'),
    path('account/logout/',logout.LogoutView,name='logout'),
    path('account/register/',register.RegisterView,name='register'),

    # rooms
    path('',get.GetAllRooms,name='rooms'),
    path('room/<str:room_id>/',get.GetRoom,name='room'),
    path('delete/room/<str:room_id>/',delete.DeleteRoom,name='delete_room'),
    path('create/room/',create.CreateRoom,name='create_room'),

]