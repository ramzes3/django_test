from django.db import models
from django.utils import timezone
# Create your models here.


class Shot_information(models.Model):
    root_folder = models.CharField(max_length=200)
    user_identifier = models.CharField(max_length=200,default='zero')
    #aquisition_date_time = models.DateTimeField('date published')
    aquisition_date = models.DateField(timezone.now())
    run = models.IntegerField(default=1)
    shot_number = models.IntegerField(default=1)

class Equipment(models.Model):
    shot = models.ForeignKey(Shot_information, on_delete=models.CASCADE,default='')
    equipment_name = models.CharField(max_length=200,default='')
    equipment_folder = models.CharField(max_length=200,default='')
    shot_number = models.IntegerField(default=1)
    n_axis = models.IntegerField(default=1)
