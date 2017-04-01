#coding=utf-8  
'''
Created on 2017年3月21日
@author: caixq
'''
import os, re

#get image file paths with extension filters
def list_pictures(directory, ext='jpg|jpeg|bmp|png'):
    return [os.path.join(root, f)
            for root, _, files in os.walk(directory) for f in files
            #if re.match('([\w]+\.(?:' + ext + '))', f)]
            #some filename contains '[' or ']'
            if re.match('([\w\[\]]+\.(?:' + ext + '))', f)]  
# return the number of images in directories
def piccounter(dir=None):
    return len(list_pictures(dir))
               
def samplecounter(train_dir=None,val_dir=None):
    return len(list_pictures(train_dir)),len(list_pictures(val_dir))

#copy data to train and validation directory
def PrepareDataSet(raw_dir,cls=[],train_dir=None,val_dir=None):
    #To-Do
    
    import os 
    import random
    import shutil
    if not os.path.exists(train_dir) :
        os.mkdir(train_dir) 
    if not os.path.exists(val_dir) :
        os.mkdir(val_dir)
    
    for folder in cls :
        
        tfold = train_dir + '/' + folder 
        vfold = val_dir + '/' + folder
        
        if not os.path.exists(tfold):
            #To-Do nested dir cannot make
            os.mkdir(tfold)   
        if not os.path.exists(vfold):
            os.mkdir(vfold)
            
        piclist = list_pictures(raw_dir +'/' +folder)
        #print (piclist)
        train_size = 0 
        vali_size = 0
        
        if len(piclist) < 10 :
            vali_size = 1 
        else :
            vali_size = len(piclist)/10
            
        train_size = len(piclist) - vali_size
        random.shuffle(piclist)
        print (folder,' val/train:', vali_size, train_size)
        count = 0
        for i in range(len(piclist)):
            
            if i < vali_size :
                shutil.copy(piclist[i],  vfold +'/' + str(i) + '.jpg')
            else :
                shutil.copy(piclist[i],  tfold +'/' + str(i) + '.jpg')
            
    return None

#list = list_pictures('..\\data\\train')
#print list
#print len(list)

