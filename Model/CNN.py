#coding=utf-8  
'''
Created on 2017年3月21日
@author: caixq
'''
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD, Adam

from Util import config
img_width, img_height = config.img_width, config.img_height
cla = cla = config.cla

def get_model(weights_path=None, dropout=0.5):
    
    from keras import backend 
    
    backendname = backend.backend()
    if( backendname == 'theano') :
        backend.set_image_dim_ordering('th') 
    else :   
        backend.set_image_dim_ordering('tf')
    
    
    model = Sequential()
    
    if( backendname == 'theano') :
        model.add(Convolution2D(64, 3, 3, input_shape=(3, img_width, img_height)))
    else :  #tensorflow version
        model.add(Convolution2D(64, 3, 3, input_shape=(img_width, img_height,3)))
        
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    
    model.add(Dropout(dropout))

    #output layer
    model.add(Dense(len(cla)))   # number of classes
    model.add(Activation('softmax')) 
    
    if weights_path:
        model.load_weights(weights_path)
        print('Load Weight:', weights_path)
    opt1 = SGD(lr=1e-5, momentum=0.9, decay=0.0, nesterov=False)
    opt2 = Adam(lr=1e-3, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

    model.compile(loss='categorical_crossentropy',  # binary_crossentropy,categorical_crossentropy
              #optimizer=opt1,
              optimizer='rmsprop',
              metrics=['accuracy'])

    return model

def ShowOutputVec(model=None,input_file=''):
    from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
    import numpy as np
    #img = load_img(testfile)  # this is a PIL image
    img = load_img(input_file, target_size=(img_width, img_height)) 
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150) #resize ?
    #convolution2d_input_1 to have 4 dimensions
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
    out = model.predict(x,batch_size=1)  #slow
    print (input_file)
    print (out) 
    #print cla[np.argmax(out)] 

