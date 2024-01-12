from django.shortcuts import redirect


def LogoutView (request) : 

    response = redirect('rooms')
    response.delete_cookie('user')
    return response


