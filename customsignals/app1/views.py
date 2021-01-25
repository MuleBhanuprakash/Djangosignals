from django.shortcuts import render, HttpResponse
from app1 import signals


# Create your views here.

def home(request):
    signals.notification.send(sender=None, request=request, user=["bhanu", "prakash"])
    return HttpResponse("this is Homepage")
