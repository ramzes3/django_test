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
from datetime import datetime
from pydoc import locate

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL, PIL.Image
import numpy as np

from .models import Shot_information, Equipment

#def index(request):
#    return HttpResponse("Hello, world. You're at the plots index.")

def getimage(request, shot_id):
        shot = get_object_or_404(Shot_information, pk=shot_id)
        listOfEquipment = shot.equipment_set.all();
        #print(shot.equipment_set.all().count())
#        if request.method=="GET": x = np.arange(0, random.randint(0,3) * np.pi, 0.01)       
#        else: x = np.arange(0, 2 * np.pi, 0.01)
#        s = np.cos(x) ** 2
#        plt.plot(x, s)
        
        #plt.xlabel('xlabel(Z)')
        #plt.ylabel('ylabel(Y)')
        #plt.title('Simple Graph!')
        #plt.grid(True)
        plt.figure(1) 
        plt.clf()
        for counter, tmp in enumerate(listOfEquipment):
           #print(tmp)
           #print(tmp.equipment_folder)
           listOfImages = [f for f in os.listdir(tmp.equipment_folder) if f.endswith('.png')]           
           ax1 = plt.subplot(3,3,counter+1)             # the first subplot in the first figure 
           #ax1.set_xticklabels([])
           #ax1.set_yticklabels([])
           #ax1.set_aspect('equal') 
           plt.axis('off')
           plt.title(tmp.equipment_name)
           #print(len(listOfImages))
           if len(listOfImages) < shot.shot_number:
                ax1.annotate('Shot not present',xy=(0.1,0.5))
                continue

           img_path = os.path.join(tmp.equipment_folder,listOfImages[shot.shot_number-1]);
           img = mpimg.imread(img_path)
           #print(tmp)
           plt.imshow(img)


        #plt.subplots_adjust(wspace=0, hspace=0)

        #path = "/media/Arni1/data/2018/20180219/run006/"
        #path = get_path(path,1)
        #print(path)
        #listOfImages = [f for f in os.listdir(path) if f.endswith('.png')]
        #img_path = os.path.join(path,listOfImages[shot.shot_number]);
        #img = mpimg.imread(img_path)
        #A=np.asarray(img)
        #plt.imshow(img)


        response = HttpResponse(content_type="image/png")
        plt.savefig(response, format="png",bbox_inches='tight')

        return response

def display_shot(request, shot_id):
        shot = get_object_or_404(Shot_information, pk=shot_id)
        #if request.method !== 'POST':
        #     return HttpResponse("There is no data submitted")
        #r_type = locate(shot.run)
        if ('Previous' in request.POST) and (shot.shot_number>1):
             shot.shot_number = shot.shot_number-1
        elif('Next' in request.POST):
             shot.shot_number = shot.shot_number+1
        else:
             shot.shot_number = int(request.POST['Shot_number'])

        run = int(request.POST['Run'])
        date = datetime.strptime(request.POST['Date'], "%Y-%m-%d").date()
        if (shot.run != run) or (shot.aquisition_date != date):
             status_change=1
        else:
             status_change=0

        shot.run = request.POST['Run']
        shot.aquisition_date = datetime.strptime(request.POST['Date'], "%Y-%m-%d").date()
        shot_dir = get_shot_dir(request, shot) 
        
        if not os.path.isdir(shot_dir):
             print(shot_dir)
             return HttpResponse("There is no data available on this day")
       
        listOfEquipment = os.listdir(shot_dir)
  
        print(listOfEquipment)
        if status_change:
             print("Change occured")
             shot.run = request.POST['Run']
             shot.aquisition_date = datetime.strptime(request.POST['Date'], "%Y-%m-%d").date()
             shot.equipment_set.all().delete()
             for tmp in listOfEquipment:
                 #print(tmp)  
                 shot.equipment_set.create(equipment_name=tmp,equipment_folder=os.path.join(shot_dir,tmp))




        #print(shot.aquisition_date)
        shot.equipment_set.all()
        shot.save()

        #print(shot.equipment_set.all().count())


        
        context = {'shot': shot, 'c_date':str(shot.aquisition_date),}
        return render(request, 'plots/display_shot.html',context)
        #return HttpResponse("Hello, world. You're at the display shots.")

def index(request):
        path = "/media/Arni1/data/"
        shot_list = Shot_information.objects.all()    
        shot = shot_list.filter(user_identifier__startswith='roman')        
        if shot.count()==0:
            Shot_information.create(root_folder=path,user_identifier="roman", aquisition_date=timezone.now())
                     

        shot = get_object_or_404(Shot_information, user_identifier='roman')
        print( str(shot.aquisition_date) )
        #shot.run = 1
        shot.root_folder = path
        shot.save()   
        context = {'shot': shot, 'c_date':str(shot.aquisition_date),}
        #shot_id = get_object_or_404(Shot_information, pk=question_id)
        return render(request, 'plots/choose_data.html',context)

def get_shot_dir(request, shot):        
        date_folder = ("".join(map(str,[shot.aquisition_date.year, str(shot.aquisition_date.month).rjust(2,'0'), str(shot.aquisition_date.day).rjust(2,'0')])))
        run_folder = ("".join(map(str,["run",str(shot.run).rjust(3,'0')])))
        path = os.path.join(shot.root_folder, str(shot.aquisition_date.year), date_folder,run_folder)

        return path


# Redundant code
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
