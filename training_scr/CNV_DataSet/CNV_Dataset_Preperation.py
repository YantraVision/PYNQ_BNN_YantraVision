from numpy import *
import idx2numpy
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps 
coll=array([])

# TBD 
# 1. Take a file list
# 2. Example Data Images
#  


for n in range("""Nimber of Images"""):
	img=Image.open("""Image Name"""{0}.format(n)).convert("L") 	#Opening the image in Monochrome version
	img
	contr = ImageEnhance.Contrast(img)
	img = contr.enhance(3)                                                  
	bright = ImageEnhance.Brightness(img)                               
	img = bright.enhance(4)  		       			#Enhancement of Contrast and Brightness
	img=ImageOps.invert(img)		       			#Invert Image (White in Black)
	img=img.resize((28,28))  		       			#Conversion of Resolution to 28 X 28
	img	
	arr=array(img)							#Conversion of Image to 2D numpy array
	for i in range(28):
   		for j in range(28):
       			if(arr[i][j]==0):
       	     			arr[i][j]=1
        		else:
            			arr[i][j]=255		       		#Concersion to MNIST Datset format
idx2numpy.convert_to_file("""File Name""",arr)           		#Conversion 2D numpy array to idx2 format
