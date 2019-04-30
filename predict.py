from keras.models import load_model
from keras.optimizers import Adam
import os
import numpy as np
model=load_model('models/model.h5')
test_X=np.load('test_X.npy')
test_Y=np.load('test_Y.npy')
print test_X.shape,test_Y.shape
print test_Y.shape[0]
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
pred=np.array(model.predict_classes(test_X))
accuracy=np.sum(pred==(test_Y-1))/float(test_Y.shape[0])
print accuracy
