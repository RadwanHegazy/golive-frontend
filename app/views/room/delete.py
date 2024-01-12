from django.http import HttpResponse
from django.shortcuts import redirect
from globals.decorators import login_required
from frontend.settings import MAIN_URL
import requests

@login_required
def DeleteRoom (request, room_id) : 


    
    user = request.COOKIES.get('user')
    req = requests.delete(
        url = f"http://127.0.0.1:4444/room/delete/{room_id}/",
        headers = {'Authorization':f"Bearer {user}"},
    )

    print(req.json())

    return redirect('rooms')


