
# coding: utf-8

# In[1]:

 


import subprocess
#command = "$wget -O horray https://patch.com/img/cdn20/users/22821259/20180112/071633/styles/T800x600/public/processed_images/newport_whitepit_lane_pot_hole-1515802556-4418.jpg?width=700"

#proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
fp = "Fotolia_80750547_Subscription_Monthly_XL.jpg"
command = "${PWD}/darknet detector test -dont_show  pothole/pothole.data pothole/pothole.cfg pothole/backup/pothole_4000.weights -ext_output %s" % fp
proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output = proc.stdout.read()


# In[16]:


type(output)

print(output)
# In[7]:


fork=['left_x:','top_y:','widht:','height:']


# In[144]:


a=str(output, 'utf-8')
a
b=a.replace(":", "")
a=b.replace(" ", "")
b=a.replace(")", "")
b


# In[193]:


j=0
f=[]
import re
for i in range(len(b)):
    try:
        found=''
        
        found = re.search('left_x(.+?)\n',b[i:]).group(1)
        if(found!=''):
            if found not in f:
                f.append(found)      
    except AttributeError:
        continue


# In[197]:


f


# In[240]:


pos1=[]
pos2=[]
pos3=[]
for i in range(len(f)):
    pos1=pos1+f[i].split('top_y')
for i in range(len(pos1)):
    pos2=pos2+pos1[i].split('width')
for i in range(len(pos2)):
    pos3=pos3+pos2[i].split('height')
pos3 = [int(i) for i in pos3]
pos3


# In[267]:


pos1=[]
pos2=[]
pos3=[]
for i in range(len(f)):
    pos1=pos1+f[i].split('top_y')
for i in range(len(pos1)):
    pos2=pos2+pos1[i].split('width')
for i in range(len(pos2)):
    pos3=pos3+pos2[i].split('height')
pos3 = [int(i) for i in pos3]
x=[]
y=[]
w=[]
h=[]
for i in range(len(pos3)):
    if((i+1)%4==1):
        x.append(pos3[i])
    if((i+1)%4==2):
        y.append(pos3[i])
    if((i+1)%4==3):
        w.append(pos3[i])
    if((i+1)%4==0):
        h.append(pos3[i])
																					type(x[0])


# In[284]:


crop_areas= [[0]*4 for i in range(len(x))]
for i in range(len(x)):
        crop_areas[i][0]=x[i]
        crop_areas[i][1]=y[i]
        crop_areas[i][2]=x[i]+w[i]
        crop_areas[i][3]=y[i]+h[i]
tuple(crop_areas)


# In[287]:


import os

from PIL import Image

# Crops the image and saves it as "new_filename"
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)


image_name =fp
img = Image.open(image_name)

# Loops through the "crop_areas" list and crops the image based on the coordinates in the list
for i, crop_area in enumerate(crop_areas):
    filename = os.path.splitext(image_name)[0]
    ext = os.path.splitext(image_name)[1]
    new_filename = "crop/"+filename + '_cropped' + str(i) + ext

    crop_image(img, crop_area, new_filename)


# In[232]:


print("no. of potholes:")
print(len(x))

print("minimum length of pothole:")
print(min(h)*0.22)

print("maximum length of pothole:")
print(max(h)*0.22)
