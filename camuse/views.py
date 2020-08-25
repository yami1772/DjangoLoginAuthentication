from django.shortcuts import render
from django.template import loader
from django import template
from django.http import HttpResponse
from .models import Camera, User
# Create your views here.

def index0(request):
    cam_list = Camera.objects.order_by('id')[:5]
    output = ', '.join([q.cam_position for q in cam_list])
    return HttpResponse(output)

def index(request):
    latest_cam_list = Camera.objects.order_by('id')[:5]
    template = loader.get_template('camuse/index.html')
    context = {
        'latest_cam_list': latest_cam_list,
    }
    return HttpResponse(template.render(context, request))



def detail(request, Camera_id):
    return HttpResponse("You're looking at Camera %s." % Camera_id)

def state(request, Camera_id):
    response = "You're looking at the state of camuse %s."
    return HttpResponse(response % Camera_id)

def cameraUser(request, Camera_id):
    return HttpResponse("You're user on camuse %s." % Camera_id)
