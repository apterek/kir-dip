from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from core.models import Faces


# Home
def index(request):
    post = Faces.objects.all()
    print(post)
    if request.method == "GET":
        return render(request, "index.html", {"post": post})
    return HttpResponse('')
