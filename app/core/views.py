from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView


# Home
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    return HttpResponse('')
