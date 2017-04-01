#coding=utf-8  
'''
Created on 2017年3月21日
@author: caixq
'''
#for Training
img_width, img_height = 200,200
#cla = ['feather','coat','sweater','long','short','vest','swimsuit','naked']
cla = ['ac','aco','bpot','cookie','ecooker','eheater','eoven','fan','foci','fruit','gheat','kettle','microwave','oven','pot','rf','soy','vclr','wash','wdisp']
cla_desc = ['空调','空调外机','电炖锅','煎烤机','电饭煲','电热水器','电磁炉','电风扇','燃气灶','蔬果机','燃气热水器','热水壶','微波炉','烤箱','炒锅','冰箱','豆浆机','吸尘器','洗衣机','饮水机']

train_data_dir = 'data/train'  #windows dir
validation_data_dir = 'data/validation'  

#for Web Serving
serv_model_path = 'model/appliance_cnn.h5'


#test
vali_model_path = 'appliance_cnn.h5'
test_pic1 = 'data/validation/ac/0.jpg'
test_pic2 = 'data/validation/microwave/0.jpg'