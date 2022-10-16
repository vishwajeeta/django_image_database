from email.policy import default
from django.db import models

# Create your models here.
class images(models.Model):
    img=models.ImageField(upload_to="alex",default="omg.jpg",null=True)
    def __str__(self):
        return f'{self.img}'