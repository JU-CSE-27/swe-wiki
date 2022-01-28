from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
"""
This is a home page
-------------------

home function

"""
def home(request):
    """
    :param name: request- render home page
    :param type: url
    :return: url
    """
    return render(request, 'home.html')

"""
This is a room page
-------------------

room function

"""
def room(request, room):
    """
    :param name: request- render room page
    :param type: url
    :return: url
    """
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    """
    :param name: request- render username
    :param type: url
    :return: none
    """
    
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    """
    :param name: request- render send
    :param type: url
    :return: none
    """
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    # return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request,  room):
    """
    :param name: request- render getMessage
    :param type: url
    :return: message
    """
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
