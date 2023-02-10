from django.shortcuts import render, HttpResponse

# Create your views here.
def HomeView(request):
    return HttpResponse("Hello, world. 962a419a is the polls index.")
