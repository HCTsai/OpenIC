#coding=utf-8  
'''
Created on 2017年3月23日
@author: caixq
'''
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np


try:
  from urllib2 import urlopen # Python2
except ImportError:
  from urllib.request import urlopen# Python3
from Util import config

img_width, img_height = config.img_width, config.img_height
cla = config.cla

def predict_by_file(model,filepath):
    #img = load_img(filepath, target_size=(img_width, img_height)) 
    img = load_img(filepath)
    p = predict_by_img(model,img)
    print ('file name: ',filepath)
    print ('output layer: ', str(p)) 
    label = np.argmax(p[0]) 
    return cla[label]

def predict_by_url(model,url):
    
    #url to image
    import io
    from PIL import Image
    image_bytes = urlopen(url).read()
    data_stream = io.BytesIO(image_bytes)
    img = Image.open(data_stream)
    #
    #some file may not 24 bit color space 
    img = img.convert('RGB')
   
    p = predict_by_img(model,img)
    
    print ('file url: ' ,url)
    print ('output layer: ' , str(p)) 
    label = np.argmax(p[0]) 
    return cla[label]   

def predict_by_img(model,img):
    
    img = img.resize((img_width, img_height))
    #some file may not 24 bit color space
    img = img.convert('RGB')
    
    x = img_to_array(img) 
    x = x.reshape((1,) + x.shape) #x = np.expand_dims(x, axis=0)
    p = model.predict(x,batch_size=1)  #slow
    #img.save('thumb.jpg') 
    return p

def predict_by_dir(model,dir):
    reslist = []
    from Util import file_process
    filelist = file_process.list_pictures(dir)
    
    for f in filelist :
       img = load_img(f)
       p = predict_by_img(model,img)
       reslist.append(np.argmax(p[0]))  
       
    return reslist