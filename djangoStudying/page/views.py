from django.http import HttpResponse
from django.shortcuts import render

def top(request):
    return render(request, 'page/top.html')