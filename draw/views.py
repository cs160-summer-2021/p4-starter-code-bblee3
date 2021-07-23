# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def qOne(request):
    return render(request, 'draw/qOne.html')

def qTwo(request):
    return render(request, 'draw/qTwo.html')

def qThree(request):
    return render(request, 'draw/qThree.html')

def qFour(request):
    return render(request, 'draw/qFour.html')

def qFive(request):
    return render(request, 'draw/qFive.html')
    
def bigScreen(request):
    return render(request, 'draw/bigScreen.html')

def bigScreenName(request):
    return render(request, 'draw/bigScreenName.html')

def thankScreen(request):
    return render(request, 'draw/thankScreen.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
