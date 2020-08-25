from django.db import models

# Create your models here.
class Camera(models.Model):
    def __str__(self):
        return self.cam_position

    cam_position = models.CharField(max_length=100)
    cam_attr = models.CharField(max_length=100)

class User(models.Model):
    def __str__(self):
        return self.cam_choiced

    cam_choiced = models.ForeignKey(
        'Camera',
        on_delete=models.CASCADE,
    )
    note_text = models.CharField(max_length=200)
    burden = models.IntegerField(default=0)