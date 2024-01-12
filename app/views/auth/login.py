from django.shortcuts import redirect, render
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def LoginView (request) : 
    context = {}
    
    if request.method == "POST" : 
        data = {
            'email' : request.POST.get('email',None),
            'password' : request.POST.get('password',None)
        }

        user = Action(
            url = MAIN_URL + "/auth/login/",
            data = data
        )

        user.post()

        if user.is_valid() : 
            response = redirect('rooms')
            response.set_cookie('user',user.json_data()['token'])
            return response
        
        context['error'] = "البيانات غير صحيحة"

    return render(request,'login.html',context)


