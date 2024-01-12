from django.shortcuts import render, redirect
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL

@login_required
def CreateRoom (request) : 

    context = {}
    if request.method == "POST" : 
        data = {
            'title' : request.POST.get('title',None)
        }

        user = request.COOKIES.get('user')

        headers = {'Authorization':f"Bearer {user}"}

        action = Action(
            url = MAIN_URL + '/room/create/',
            data = data,
            headers=headers
        )

        action.post()
        
        if action.is_valid() :
            room_id = action.json_data()['id'] 
            return redirect('room', room_id)
        
        context['error'] = "يوجد خطأ اثناء انشاء البث المباشر"

    return render(request,'room-create.html',context)


