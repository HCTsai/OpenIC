#coding=utf-8  
'''
Created on 2017年3月21日
@author: caixq
'''
from keras.preprocessing.image import ImageDataGenerator
import os 
#if "image_dim_ordering": is "th" and "backend": "theano", your input_shape must be (channels, height, width)
#if "image_dim_ordering": is "tf" and "backend": "tensorflow", your input_shape must be (height, width, channels)
from keras import backend 

#check keras backend : [theano, tensorflow]
backendname = backend.backend()
print ('Backend: ',backendname)
if( backendname == 'theano') :
    backend.set_image_dim_ordering('th') ### OverflowError: Range exceeds valid bounds
else :   #if(backendname == 'tensorflow')
    backend.set_image_dim_ordering('tf')


# dimensions of our images.
from Util import config, file_process

img_width, img_height = config.img_width, config.img_height
train_data_dir = config.train_data_dir
validation_data_dir = config.validation_data_dir
#cla = ['feather','coat','sweater','long','short','vest','swimsuit','naked']
cla = config.cla
#need to change dynamic counting

nb_train_samples = file_process.piccounter(train_data_dir) #11485
nb_validation_samples = file_process.piccounter(validation_data_dir)
print ('[nb_train,nb_valudation]=',nb_train_samples,nb_validation_samples)
#number of epoch per run
nb_epoch = 1
weightname = config.vali_model_path

#Network Structure
from Model import CNN as cnn 

if (os.path.exists(weightname)) :
    model = cnn.get_model(weightname, 0.5)
    print ('load weight file: ', weightname) 
else:
    model = cnn.get_model(None, 0.5)
    print ('Training new weight', weightname)
    

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rotation_range=4,
        width_shift_range=0.05,  # 2017.03.24
        height_shift_range=0.05, # 2017.03.24
        rescale=1./255,
        shear_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True)


# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=64,
        classes=cla,
        class_mode='categorical')  # class_mode?

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=64,
        classes=cla,
        class_mode='categorical')

def ShowCurrentOutput() :
   
     
    cnn.ShowOutputVec(model, config.test_pic1)
    cnn.ShowOutputVec(model, config.test_pic2)
    

run = 400000 
for i in range(0, run):
    print ('run: ',str(i))
    #
    model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples)

    model.save_weights(weightname,overwrite=True)
    ShowCurrentOutput()
    
    