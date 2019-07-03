
# coding: utf-8

# In[1]:


import subprocess
s=['/home/abhishek/Desktop/pred/31.09004.jpg',
'/home/abhishek/Desktop/pred/41.742054.jpg',
'/home/abhishek/Desktop/pred/50.192074.jpg',
'/home/abhishek/Desktop/pred/60.521774.jpg',
'/home/abhishek/Desktop/pred/70.17515.jpg',
'/home/abhishek/Desktop/pred/80.57233.jpg',
'/home/abhishek/Desktop/pred/89.13249.jpg']
for e in range(len(s)):
	fp = s[e]
	command = "${PWD}/darknet detector test -dont_show  pothole/pothole.data pothole/pothole.cfg pothole/backup/pothole_7000.weights -ext_output %s" % fp
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	output = proc.stdout.read()


# In[6]:


#output


# In[4]:


	fork=['left_x:','top_y:','widht:','height:']


# In[5]:


	a=str(output, 'utf-8')
	a
	b=a.replace(":", "")
	a=b.replace(" ", "")
	b=a.replace(")", "")
	b


# In[7]:


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
	
	
# In[20]:


	f


# In[9]:


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
	
	
	# In[11]:
	
	
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
#type(x[0])


# In[21]:


	x,y,w,h


# In[14]:


	crop_areas= [[0]*4 for i in range(len(x))]
	for i in range(len(x)):
	        crop_areas[i][0]=x[i]
	        crop_areas[i][1]=y[i]
	        crop_areas[i][2]=x[i]+w[i]
	        crop_areas[i][3]=y[i]+h[i]
	tuple(crop_areas)
	
	
# In[15]:


	import os

	from PIL import Image

# Crops the image and saves it as "new_filename"
	def crop_image(img, crop_area, new_filename):
	    cropped_image = img.crop(crop_area)
	    cropped_image.save(new_filename)
	
# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)


	
	q=s[e].rfind('/')
	k=s[e][q+1:]

	image_name =k
	img = Image.open(image_name)
	
	# Loops through the "crop_areas" list and crops the image based on the coordinates in the list
	for i, crop_area in enumerate(crop_areas):
	    filename = os.path.splitext(image_name)[0]
	    ext = os.path.splitext(image_name)[1]
	    new_filename = "crop/"+filename +'_'+str(h[i]*0.022)+'-' + str(i) + ext
	
	    crop_image(img, crop_area, new_filename)
	
	
# In[18]:


	crop_areas


# In[22]:


print("no. of potholes:")
print(len(x))
for z in range(len(h)):
	print("length of pothole:",z)
	print((h[z])*0.022)
	print("breadth of pothole:")
	print((w[z])*0.022)
