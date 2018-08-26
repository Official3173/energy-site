from django.http import HttpResponse
from django.shortcuts import render
from .models import User

def index(request):
    
    my_info = { 'name': 'Mitchell', 'age': '28', 'url': 'admin/'}
    return render(request, 'images/index.html', my_info)


def detail(request, album_id):
    return HttpResponse('<h1>Success! Details for album, from newboston tut. ID: ' + str(album_id) +'</h1>')

def math(request):
    return render(request, 'images/math.html')

def answer(request):
    return render(request, 'images/answer.html')



