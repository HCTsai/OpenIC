#coding=utf-8  
'''
Created on 2017年3月15日
@author: caixq
'''
# main.py
# coding:utf-8
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL

'''
'''
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD, Adam
import os 
import io
from PIL import Image

from keras import backend 
import time 

app = Flask(__name__)
files = UploadSet('files', ALL)
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'
configure_uploads(app, files)


'''
load model in global
'''
import sys
sys.path.append('../')


from Util import config

from flask import jsonify  
import json
from WebServ import classifier



#load model in global
classifier.load_model()


@app.route('/classify', methods=['GET', 'POST'])
def upload():
    
    #import uuid
    #temppic = 'static/' + str(uuid.uuid1())+ '.jpg'
    if request.method == 'POST' and 'media' in request.files:
        st = time.time()
        
        image_file = request.files['media']
        #filename = files.save(image_file)
        #data_stream = io.BytesIO(image_bytes)
        img = Image.open(request.files['media']) #PIL Image open
        #img = img.convert('RGB')
       
       
        print ('file name: ' ,image_file.filename)
              
        labeldesc, distrib= classifier.GetClassifyResult(img)       
        r = {}
        r['label'] = labeldesc
        r['v'] = str(distrib)
        return jsonify(r)
        #return jsonify(label=labeldesc, v=str(p[0]))
    
    else :     
        #return render_template('upload_jqprev.html')
        return render_template('upload_loadimg.html')
    #return render_template('upload.html') 

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)