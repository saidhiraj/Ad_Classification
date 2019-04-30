# Ad_Classification
Classifying Advertisements into various topics using Neural Networks.

The codes are for Preprocessing,Feature_extraction,Training,Testing.
These codes also work with python 3

Libraries used:

Keras	2.2.4
Keras-Applications	1.0.7
Keras-Preprocessing	1.0.9
numpy                   1.15.4
python                  2.7.12
opencv                  4.1.0
tensorflow              1.13.1

Dataset:

Images:
Our image dataset contains a total of 64,832 advertisement images.Images are split into 11 folders (subfolder-0 to subfolder-10).
To obtain the dataset, please just download all compressed zip files and extract them all into the same folder.

https://storage.googleapis.com/ads-dataset/subfolder-0.zip
https://storage.googleapis.com/ads-dataset/subfolder-1.zip
https://storage.googleapis.com/ads-dataset/subfolder-2.zip
https://storage.googleapis.com/ads-dataset/subfolder-3.zip
https://storage.googleapis.com/ads-dataset/subfolder-4.zip
https://storage.googleapis.com/ads-dataset/subfolder-5.zip
https://storage.googleapis.com/ads-dataset/subfolder-6.zip
https://storage.googleapis.com/ads-dataset/subfolder-7.zip
https://storage.googleapis.com/ads-dataset/subfolder-8.zip
https://storage.googleapis.com/ads-dataset/subfolder-9.zip
https://storage.googleapis.com/ads-dataset/subfolder-10.zip 

Image annotations:
http://people.cs.pitt.edu/~kovashka/ads/annotations_images.zip

All subfolders except ninth folder are combined to make training dataset.
Ninth subfolder is used as testing dataset.

Preprocessing:
Code for preprocessing is in resize.py,preprocess.py,onehot.py
 
There are 38 topics in this dataset.Each topics has three classifications and we need to choose the frequent one.Some samples have 3 different classifications.The labels for these sampels are obtained by random sampling out of three classes given to that sample.If the topics class is not in 38 topics or not clear,that sample is labeled as Unclear resulting in 39 possible labels for each sample.
All the images (training,testing) are resized to (224,224,3) RGB images.
The class numbers of each data sample in training set are converted into one hot encoded vectors of size 39.These vectors are stored as train_Y.npy files.

Feature extraction:
The code for feature extraction is in get_features.py

The code reads the images of training and testing dataset using opencv and stores the pixel values of images in train_X.npy files. 

Training:
The code for training is available in train.py.The features of training dataset and also one_hot labels are loaded from respective .npy files.

Keras resnet50 model is used for training the model.
Trained model is saved in model.h5 file and model weights are saved in weights.h5 file. 

Testing:
The code for testing is available in predict.py

The extracted features of the test dataset using get_features.py are used as input to test the model and accuracy is used as an evaluation metric.
