from django.shortcuts import render
from django.http import HttpResponse
from camuse.models import Camera, User
# Create your views here.

def index(request):
    cam_list = Camera.objects.order_by('id')[:5]
    output = ', '.join([q.cam_position for q in cam_list])
    return HttpResponse(output)


def detail(request, Camera_id):
    return HttpResponse("You're looking at Camera %s." % Camera_id)

def state(request, Camera_id):
    response = "You're looking at the state of camuse %s."
    return HttpResponse(response % Camera_id)

def cameraUser(request, Camera_id):
    return HttpResponse("You're user on camuse %s." % Camera_id)
