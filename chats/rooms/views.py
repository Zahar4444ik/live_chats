from django.shortcuts import render, redirect
from .models import Room, Message

from django.contrib.auth.decorators import login_required

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:30]

    return render(request, 'rooms/room.html', {'room': room, 'messages': messages})

def clean_chat(request, slug):
    room = Room.objects.get(slug=slug)
    Message.objects.filter(room=room).delete()
    return redirect('room', slug=slug)


