from django.shortcuts import render
import random
#from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def password(request):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

    n = int(request.GET.get('length'))
    g_password = ""

    if request.GET.get('uppercase'):
        letters.extend(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    if request.GET.get('special'):
        letters.extend(['!', '#', '$', '%', '&', '(', ')', '*', '+'])
    if request.GET.get('numbers'):
        letters.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    for _ in range(n):
        g_password += random.choice(letters)

    return render(request, 'password.html', {'password': g_password})