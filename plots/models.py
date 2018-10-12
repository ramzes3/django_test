from django.db import models
from django.utils import timezone
# Create your models here.


class Equipment(models.Model):
    equipment_name = models.CharField(max_length=200)
    n_axis = models.IntegerField(default=0)
    
class shot_information(models.Model):
    root_folder = models.CharField(max_length=200)
    user_identifier = models.CharField(max_length=200,default='zero')
    #aquisition_date_time = models.DateTimeField('date published')
    aquisition_date = models.DateField(timezone.now())
    run = models.IntegerField(default=1)
    shot = models.IntegerField(default=1)
