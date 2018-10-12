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

def index(request):
    return HttpResponse("Hello, world. You're at the plots index.")

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

def inter(request, image_id):
        path = "/media/Arni1/data/2018/20180219/run006/"
        listOfEquipment = os.listdir(path)
        for tmp in listOfEquipment:
             print(tmp)        

        image_id =1
        return render(request, 'plots/inter.html',{'image_id': image_id})

def next_image(request, image_id):

        path = "/media/Arni1/data/2018/20180219/run006/"       
        image_id +=1

        return render(request, 'plots/inter.html',{'image_id': image_id})

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

     
def index(request):
        path = "/media/Arni1/data/2018/"
        shot_list = shot_information.objects.all()    
        shot_id = shot_list.filter(user_identifier__startswith='roman')        
        if shot_id.count()==0:
            shot_id.create(root_folder=path,user_identifier="roman", aquisition_date=timezone.now())

        shot_id = get_object_or_404(shot_information, user_identifier='roman')
        print( shot_id.shot )
        shot_id.shot = 3
        shot_id.save();
        #shot_id = get_object_or_404(shot_information, pk=question_id)
        return render(request, 'plots/choose_data.html',{'shot_id': shot_id})

#return HttpResponse("Hello, world. You're at the plots index.")


#def choose_data(request,image_id):



