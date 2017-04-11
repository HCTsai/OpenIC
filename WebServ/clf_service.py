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
#save upload files
'''
files = UploadSet('files', ALL)
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'
configure_uploads(app, files)
'''


@app.route('/fileclf', methods=['GET', 'POST'])
def clf_upload():
    #import uuid
    #temppic = 'static/' + str(uuid.uuid1())+ '.jpg'
    
    if request.method == 'POST' and 'media' in request.files:
       
        image_file = request.files['media']
        #save files by flask_uploads
        #filename = files.save(image_file)
        img = Image.open(image_file) #PIL Image open
        #print ('file name: ' ,image_file.filename)
        labeld, dist = classifier.GetClfResbyImg(img)       
       
        r = {}
        r['label'] = labeld
        r['v'] = str(dist)
        return jsonify(r)
        #return jsonify(label=labeldesc, v=str(p[0]))
    
    else :     
        return render_template('upload_jqprev.html')
        #return render_template('upload_loadimg.html')
    #return render_template('upload.html') 

@app.route('/urlclf', methods=['GET', 'POST'])
def clf_url():
    print (request.files)
    print (request.form) 
    if request.method == 'POST' and 'url' in request.form:
        #get url string
        url = request.form['url']
        print ('usr_url: ', url)
        labeld, dist = classifier.GetClfResbyUrl(url)       
        
        r = {}
        r['label'] = labeld
        r['v'] = str(dist)
        return jsonify(r)
    elif  request.method == 'POST' and 'media' in request.files :
            
        image_file = request.files['media']
        #save files by flask_uploads
        #filename = files.save(image_file)
        img = Image.open(image_file) #PIL Image open
        #print ('file name: ' ,image_file.filename)
        labeld, dist = classifier.GetClfResbyImg(img)       
        
        r = {}
        r['label'] = labeld
        r['v'] = str(dist)
        return jsonify(r)
        
    else :     
        return render_template('url_prev.html')
        #return render_template('upload_loadimg.html')
    #return render_template('upload.html') 

def ret_resp(labeld,dist):
    r = {}
    r['label'] = labeld
    r['v'] = str(dist)
    return jsonify(r)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)