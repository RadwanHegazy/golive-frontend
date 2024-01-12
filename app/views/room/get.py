from django.http import HttpResponse, Http404
from django.shortcuts import render
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from globals.user import userTemp

def GetAllRooms (request) : 
    context = {}

    process = Action(
        url = MAIN_URL + "/room/get/"
    )

    process.get()

    context['rooms'] = process.json_data()
    return render(request,"home.html",context)


def GetRoom (request, room_id) : 
    
    context =  {}
    action = Action(
        url = MAIN_URL + f'/room/get/{room_id}/'
    )

    action.get()


    user = userTemp(request)


        
    if not action.is_valid() : 
        raise Http404(request)
    
    context['room'] = action.json_data()

    room_url = f'http://127.0.0.1:8000/room/{room_id}/'
    context['room_url'] = room_url
    
    if user['c_user'] : 
        return render(request,'room-admin.html',context)

    return render(request,'room-user.html',context)

