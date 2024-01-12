from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def RegisterView (request) : 
    
    context = {}

    if request.method == "POST" : 
        data = {
            "full_name" : request.POST.get('full_name',None),
            "email" : request.POST.get('email',None),
            "password" : request.POST.get('password',None),
        }


        user = Action(
            url = MAIN_URL + "/auth/register/",
            data = data,
        )

        if request.FILES : 
            picture = request.FILES['picture']
            user.files = {
                'picture' : picture
            }
        
        user.post()

        if user.is_valid() : 
            response = redirect('rooms')
            response.set_cookie('user',user.json_data()['token'])
            return response
        context['error'] = 'البيانات غير صحيحة'

    return render(request,'register.html',context)


