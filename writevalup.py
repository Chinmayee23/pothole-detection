# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:42:46 2019

@author: Chinmayefile:///E:/pascal voc
# -*- coding: utf-8 -*-

Created on Thu Feb 14 17:38:20 2019

@author: Chinmayee
"""

# -*- coding: utf-8 -*-	
"""
Created on Thu Feb 14 16:11:50 2019

@author: Chinmayee"""	
import csv	
import os	
import pandas as pd

gyro={}	
index={}	
height={}	
row={}	
a=[]
	
files=os.listdir("E:/deep blue/123/")	
print(files[0])	
filestr=str(files[0])	
n=len(files)	
for j in range(0,n):
    filestr=str(files[j])	
    gy=filestr.split('_',1)
    gyro[j]=gy[0]	
    h=gy[1].split('-',1)
    height[j]=h[0]	
    i=h[1].split('.',1)
    index[j]=i[0]	

print(gyro)	
print(height)	
print(index)


    
for j in range(0,n):
    if((index[j])in(a)):
        continue
    a.append(index[j])	
    
    for i in range(0,n):
        if(index[i]==a):	
            row[0]=index[i]	
            if((float(gyro[i])>=25)and(float(gyro[i])<35)):	
                row[1]=height[i]	
                print(row[1])
            if((float(gyro[i])>=35)and(float(gyro[i])<45)):	
                row[2]=height[i]
                print(row[2])	
            if((float(gyro[i])>=45)and(float(gyro[i])<55)):	
                row[3]=height[i]
                print(row[3])	
            if((float(gyro[i])>=55)and(float(gyro[i])<65)):	
                row[4]=height[i]
                print(row[4])	
            if((float(gyro[i])>=65)and(float(gyro[i])<75)):	
                row[5]=height[i]
                print(row[5])	
            if((float(gyro[i])>=75)and(float(gyro[i])<85)):	
                row[6]=height[i]
                print(row[6])	
            if((float(gyro[i])>=85)and(float(gyro[i])<95)):	
                row[7]=height[i]
                print(row[7])	

    with open('E:\deep blue\depth_pothole.csv','w',newline='') as csvFile:
        writer = csv.writer(csvFile)	
        print(row)
        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
        
pd.read_csv('depth_pothole.csv').T.to_csv('output.csv',header=False)
dataset=pd.read_csv('output.csv')
dataset=dataset.fillna(method='ffill',limit=3)
dataset.T.to_csv('depth.csv',header=False)
	
csvFile.close()	
