#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:26:10 2019

@author: maxence
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:43:16 2019

@author: maxence
"""
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import  MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

from keras.utils import to_categorical


import tensorflow as tf

# Initialisation CNN

classifier = Sequential()


# Etape 1 - Convolution

classifier.add(Convolution2D(filters=32, 
                             kernel_size=3, 
                             strides=1, 
                             input_shape=(500, 500, 3), 
                             activation="relu" ))

# Etape 2 - Pooling

classifier.add(MaxPooling2D(pool_size=(2, 2) ))

# 2 eme couche 
classifier.add(Convolution2D(filters=32, 
                             kernel_size=3, 
                             strides=1,     
                             activation="relu" ))
classifier.add(MaxPooling2D(pool_size=(2, 2) ))


# Etape 3 - Flattening

classifier.add(Flatten())

# Etape 4 - ANN Connected

classifier.add(Dense(units=128, activation="relu"))
classifier.add(Dense(units=36, activation="softmax"))

#Completion

classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(500, 500),
        batch_size=32,
        class_mode="categorical")

validation_generator = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(150, 150),
        batch_size=32,
        
        class_mode="categorical")
print(2)
classifier.fit_generator(
        training_set,
        steps_per_epoch=250,
        epochs=25,
        validation_data=validation_generator,
        validation_steps=63)


# test single prédiciton
import numpy as np
from keras.preprocessing import image

test_image = image.load_img("dataset/single_prediction/predict18.jpg",
                            target_size=(64, 64))

test_image = image.img_to_array(test_image)

test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices

print(2)