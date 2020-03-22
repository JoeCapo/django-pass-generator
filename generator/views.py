from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def aboutme(request):
    return render(request, 'generator/aboutme.html')

def password(request):
    finalPass = ''
    char = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        char.extend(list('!@#$%&*'))
    if request.GET.get('numbers'):
        char.extend(list('1234567890'))

    for x in range(length):
        finalPass += random.choice(char)

    return render(request, 'generator/password.html', {'password': finalPass})
