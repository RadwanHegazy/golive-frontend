from django.http import HttpResponse
from globals.decorators import login_required


@login_required
def DeleteRoom (request, room_id) : 
    return HttpResponse("DeleteRoom")


