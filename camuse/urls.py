from django.urls import path

from . import views

urlpatterns = [
    # ex: /camuse/
    path('', views.index, name='index'),
    # ex: /camuse/test/
    path('test/',  views.test, name='test'),
    # ex: /camuse/5/
    path('<int:Camera_id>/', views.detail, name='detail'),
    # ex: /camuse/5/state/
    path('<int:Camera_id>/state/', views.state, name='state'),
    # ex: /camuse/5/cameraUser/
    path('<int:Camera_id>/cameraUser/', views.cameraUser, name='cameraUser'),
]