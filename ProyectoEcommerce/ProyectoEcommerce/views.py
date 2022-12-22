from django.http import HttpResponse
from django.shortcuts import render,redirect

def welcome_page(request):
    return render(request, 'welcome.html', context={})
