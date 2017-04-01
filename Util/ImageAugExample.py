#coding=utf-8  
'''
Created on 2017年3月21日
@author: caixq
'''
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

img = load_img('..\\data\\train\\coat\\1_03c76157e00b446fa586b354e01c10c3.jpg')  # this is a PIL image
img.resize((150,150))
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
img_count = 10
save_dir= 'aug_preview'
if (not os.path.exists(save_dir)) :
    os.makedirs(save_dir) 

for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=save_dir, save_prefix='c', save_format='jpeg'):
    i += 1
    if i > img_count :
        break  # otherwise the generator would loop indefinitely
print ('generate image augment: ', save_dir , img_count )