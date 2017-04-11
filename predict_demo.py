#coding=utf-8  
'''
Created on 2017年3月22日
@author: caixq
'''

from Model import predictor
from Model import CNN as cnn
#

#check keras backend : [theano, tensorflow]
'''
backendname = backend.backend()
if( backendname == 'theano') :
    backend.set_image_dim_ordering('th') 
else :   
    backend.set_image_dim_ordering('tf')
''' 
#get model from weight file
from Util import config
model = cnn.get_model(config.vali_model_path, 0)

#classify from file

filepath='data/train/ac/10.jpg' 
cls_label = predictor.predict_by_file(model, filepath)
print cls_label

#classify from url
#

url='http://img01.sogoucdn.com/app/a/100520021/7030ce6ddcf0741cbd227e59fe39a302'  #vest
cls_label = predictor.predict_by_url(model, url)
print cls_label

url='http://img1.utuku.china.com/0x0/game/20160524/551178e6-61b5-4e8f-9f48-9ac5ec072c3a.jpg'  #swimsuit
cls_label = predictor.predict_by_url(model, url)
print cls_label

url='http://www.iyi8.com/uploadfile/2015/0318/20150318125757634.jpg'  #test
cls_label = predictor.predict_by_url(model, url)
print cls_label
