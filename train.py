from keras.preprocessing import image
from keras.applications import resnet50, inception_v3, vgg16
from keras.models import Model,Sequential
from keras.layers import Dense, GlobalAveragePooling2D, Input,Flatten
from keras.optimizers import Adam
from keras.applications.resnet50 import ResNet50
import random
from PIL import Image
import json
import os
import numpy as np
model=Sequential()
model.add(ResNet50(include_top=False, weights='imagenet',pooling='avg',
                       input_tensor=None, input_shape=(224,224,3)))
model.add(Dense(39, activation='softmax', name='fc39'))
model.layers[0].trainable=False
model.summary()
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
train_X=np.load('train_X.npy')
train_Y=np.load('train_Y.npy')
print train_X.shape
print train_Y.shape
model.fit(train_X, train_Y,validation_split=0.15, epochs=50)
target_dir = './models/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
model.save('./models/model.h5')
model.save_weights('./models/weights.h5')

