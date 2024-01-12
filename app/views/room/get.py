from django.http import HttpResponse


def GetAllRooms (request) : 
    return HttpResponse("GetAllRooms")


def GetRoom (request, room_id) : 
    return HttpResponse("GetRoom")
