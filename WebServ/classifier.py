#coding=utf-8  
'''
Created on 2017年3月24日
@author: caixq
'''

from Util import config
from Model import CNN as cnn, predictor
import numpy as np
import time 


#tensorflow version 

from keras import backend 
backendname = backend.backend()
#import tensorflow as tf
#graph = tf.get_default_graph()
graph = None
if( backendname == 'tensorflow') :
    import tensorflow as tf
    graph = tf.get_default_graph()
    pass

model = None

def load_model() :
    
    from keras import backend 
    
       
    loadstart = time.time()
    img_width, img_height = config.img_width, config.img_height
    #model = cnn.get_model('model\clothes_8_cnn.h5',0.0,'theano')
    global model
    model = cnn.get_model()
    model.load_weights(config.serv_model_path)
    loadend = time.time() 
    print ('Load Model Elapse: ',str(loadend-loadstart))

def clf(img):
    
    st = time.time()
    global model
    
     # tensorflow version 
    # global graph
    # with graph.as_default():
    if( backendname == 'tensorflow') :
        global graph
        with graph.as_default():
            p = predictor.predict_by_img(model, img)
    else :
        p = predictor.predict_by_img(model, img)
        
    label = np.argmax(p[0]) 
    et = time.time()
    
    print ('output layer: ' , str(p)) 
    print ('label:',config.cla[label])
    print ('Run Model Elapse(sec.): ',str(et-st))
    #To-Do p[0] contains 'newline'
    return label , p[0]
        
#cla = ['feather','coat','sweater','long','short','vest','swimsuit','naked']
def GetClfResbyImg(img):
    
    label, dist = clf(img)
    
    if(label < len(config.cla_desc) ) :
        label = config.cla_desc[label] 
    else :
        label = str(label)
    return label, dist

def GetClfResbyUrl(url):
    #url library
    try:
        from urllib2 import urlopen # Python2
    except ImportError:
        from urllib.request import urlopen# Python3
        
    #url to image
    import io
    from PIL import Image
    image_bytes = urlopen(url).read()
    data_stream = io.BytesIO(image_bytes)
    img = Image.open(data_stream)
    #TO-Do verify image    
    #
    return GetClfResbyImg(img)
    