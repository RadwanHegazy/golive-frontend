from django.http import HttpResponse


def LogoutView (request) : 
    return HttpResponse("LogoutView")


