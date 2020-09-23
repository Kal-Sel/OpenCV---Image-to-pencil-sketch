#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


#import the library
import cv2


# In[3]:


#get the image location and the image file name
img_location = 'C:/Users/Kal-Seli/Desktop/'


# In[4]:


filename = 's.jpg'


# In[5]:


#read in the image
img = cv2.imread(img_location+filename)


# In[6]:


#convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[7]:


#invert the image
inverted_gray_image = 255 - gray_image


# In[8]:


#blur the image by gaussian blur
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)


# In[9]:


#invert the blurred image
inverted_blurred_image = 255 - blurred_image


# In[10]:


#create the pencil sketch image
pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)


# In[11]:


#show the image
cv2.imshow('Original Image', img)


# In[12]:


cv2.imshow('New Image', pencil_sketch_image)


# In[ ]:


cv2.waitKey(0)

