from django.shortcuts import render

def index(request):
    print("TEST")
    return render(request, "display/index.html", dict())
