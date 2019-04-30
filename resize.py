import os
import cv2
t=0
n=len(os.listdir('ad_images/9'))
for img in os.listdir('ad_images/9'):
	imag=cv2.imread('ad_images/9/'+img)
	new_img=cv2.resize(imag,(224,224))
	cv2.imwrite('ad_images/9/'+img,new_img)
#	print imag.shape
	if imag.shape==(224,224,3):
		t=t+1
		print(t)
print(t,n)
