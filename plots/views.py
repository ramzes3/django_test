from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.utils import timezone

# Create your views here.

from django.http import HttpResponse
from matplotlib import pylab
from pylab import *

import random
from io import StringIO
import os, sys

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL, PIL.Image
import numpy as np

from .models import shot_information

#def index(request):
#    return HttpResponse("Hello, world. You're at the plots index.")

def getimage(request, image_id):

#        if request.method=="GET": x = np.arange(0, random.randint(0,3) * np.pi, 0.01)       
#        else: x = np.arange(0, 2 * np.pi, 0.01)
#        s = np.cos(x) ** 2
#        plt.plot(x, s)

        #plt.xlabel('xlabel(Z)')
        #plt.ylabel('ylabel(Y)')
        #plt.title('Simple Graph!')
        #plt.grid(True)
        path = "/media/Arni1/data/2018/20180219/run006/"
        path = get_path(path,1)
        print(path)
        listOfImages = [f for f in os.listdir(path) if f.endswith('.png')]
        img_path = os.path.join(path,listOfImages[image_id]);
        img = mpimg.imread(img_path)
        #A=np.asarray(img)
        plt.imshow(img)


        response = HttpResponse(content_type="image/png")
        plt.savefig(response, format="png")

        return response

def next_image(request, shot_id):
        shot = get_object_or_404(Question, pk=question_id)
        path = "/media/Arni1/data/2018/20180219/run006/"       
        image_id +=1

        return render(request, 'plots/display_shot.html',{'shot_id': shot_id})

def previous_image(request, image_id):
        path = "/media/Arni1/data/2018/20180219/run006/"
        path = get_path(path,1)
        if image_id <1:
          image_id = 1
        else:
          image_id-=1

        print(image_id)
        return render(request, 'plots/inter.html',{'image_id': image_id})

def get_path(request, equipment_id):
        path = "/media/Arni1/data/2018/20180219/run006/"
        listOfEquipment = os.listdir(path)
        path = os.path.join(path, listOfEquipment[equipment_id])

        return path

def inter(request, image_id):
        path = "/media/Arni1/data/2018/20180219/run006/"
        listOfEquipment = os.listdir(path)
        for tmp in listOfEquipment:
             print(tmp)        

        image_id =1
        return render(request, 'plots/inter.html',{'image_id': image_id})

def display_shot(request, shot_id):
        shot = get_object_or_404(shot_information, pk=shot_id)
        print( shot.root_folder)
        print(get_shot_dir(request, shot))
        return HttpResponse("Hello, world. You're at the display shots.")

def index(request):
        path = "/media/Arni1/data/"
        shot_list = shot_information.objects.all()    
        shot = shot_list.filter(user_identifier__startswith='roman')        
        if shot.count()==0:
            shot.create(root_folder=path,user_identifier="roman", aquisition_date=timezone.now())
                     

        shot = get_object_or_404(shot_information, user_identifier='roman')
        #print( shot.aquisition_date )
        #shot.run = 1
        shot.root_folder = path
        shot.save()   
        context = {'shot': shot,}
        #shot_id = get_object_or_404(shot_information, pk=question_id)
        return render(request, 'plots/choose_data.html',context)

def get_shot_dir(request, shot):        
        date_folder = ("".join(map(str,[shot.aquisition_date.year, shot.aquisition_date.month, shot.aquisition_date.day])))
        run_folder = ("".join(map(str,["run",str(shot.run).rjust(3,'0')])))
        path = os.path.join(shot.root_folder, date_folder,run_folder)

        return path



