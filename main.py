# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 03:15:43 2024

@author: ranaa
"""


#Saturated contrast stretch
import numpy as np
from matplotlib import pyplot as plt
import cv2

#To read the image
img=cv2.imread("D:\\Project\\unsaturated 7.jpeg",0)


plt.subplot(231)
plt.title(" Histogram of Original Image")
plt.hist(img.ravel(),bins=255,range=(1,img.ravel().max()))

plt.subplot(234)
plt.title("Original Image ")
plt.imshow(img,cmap='gray')

#To find max 
max_img=np.max(img)
print("Max of img :",max_img)

#To find min 
min_img=np.min(img)
print("Min of img :",min_img)

#To calculate bins value
bins=max_img-min_img
print("Value of bins :",bins)

#To find total number of pixels from histogram
h=np.histogram(img,bins,(min_img,max_img))[0]
print("No of pixels :",h)

#To apply min-max stretch 
str_img=255*((img-min_img)/(max_img-min_img))

plt.subplot(232)
plt.title("Histogram of Stretched Image ")
plt.hist(str_img.ravel(),bins=255,range=(1,str_img.ravel().max()))

plt.subplot(235)
plt.title("Stretched Image ")
plt.imshow(str_img,cmap='gray')


#To find tL and tU
tL=np.percentile(str_img,1).astype(int)
tU=np.percentile(str_img,99).astype(int)
print("Lower threshold :",tL)
print("Upper threshold :",tU)

#To apply percentile stretch
#To find points below threshold value
below_tL = np.asarray(str_img < tL)

str_img[below_tL] = tL

print("points below lower threshold:",str_img)

#To find points above the upper threshold
above_tU = np.asarray(str_img > tU)

str_img[above_tU] = tU

print("points above upper threshold:",str_img)

#To set pixels between tL and tU values
str_img=((str_img-tL)/(tU-tL))*255
print("percentile stretch image :",str_img)

#To plot subgraphs of images and histograms

plt.subplot(233)
plt.title(" Histogram of Saturated contrast stretch Image")
plt.hist(str_img.ravel(),bins=255,range=(1,str_img.ravel().max()))



plt.subplot(236)
plt.title("Percentile Stretched Image ")
plt.imshow(str_img,cmap='gray')


