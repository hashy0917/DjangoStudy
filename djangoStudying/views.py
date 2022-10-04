from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world.")

def top(request):
    if request.method == 'POST':
        if "start_button" in request.POST:
            print("start")
            return render(request, 'top.html')
#        elif "finish_button" in request.POST:
#            print("finish")
    return render(request, 'top.html')