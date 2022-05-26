from django.shortcuts import render, HttpResponse, redirect
import uuid
from .models import *


def home(request):
    return render(request, "home.html")


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        url = Url(link=link, uuid=uid)
        url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://' + url_details.link)