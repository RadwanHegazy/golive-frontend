from django.shortcuts import render
from globals.decorators import login_required


@login_required
def CreateRoom (request) : 
    return render(request,'room-admin.html')


