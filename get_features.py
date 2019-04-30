import cv2 
import json
import numpy as np
import os
with open('image/onehot_topics.json','r') as f:
	data=json.load(f)
data=dict((key.encode("utf-8"),value) for (key,value) in data.items() )
#print data
train_X=[]
#print train_X.shape
train_Y=[]
n=len(os.listdir('ad_images/train'))
t=0
for img in os.listdir('ad_images/train'):
	t=t+1
	try:
		train_Y.append(data[img.replace('_','/')])
	except:
		print img
		continue
	train_X.append(cv2.cvtColor(cv2.imread('ad_images/train/'+img),cv2.COLOR_BGR2RGB))		
	print(t,n)
#print np.array(train_X).shape
#print np.array(train_Y).shape

train_X=np.array(train_X)
train_Y=np.array(train_Y)
np.save('train_X.npy',train_X)
np.save('train_Y.npy',train_Y)
print (train_X.shape,train_Y.shape)

