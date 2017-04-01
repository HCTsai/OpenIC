#coding=utf-8  
'''
Created on 2017年3月25日
@author: caixq
'''

from Model import predictor
from Model import CNN as cnn
import time 
from h5py.h5f import ACC_EXCL

#To-Do change to more flexable
from Util import config 
model = cnn.get_model(config.vali_model_path , 0)
#root = config.validation_data_dir
root = config.train_data_dir
#dirs = ['feather','coat','sweater','long','short','vest','swimsuit','naked']
#answers = [[0,1],[0,1],[2,3],[2,3],[4,5],[4,5],[6,7],[6,7]]
#answers = [[0,1],[0,1,2,3],[1,2,3],[2,3],[4,5],[4,5],[6,7],[6,7]]
#answers = [[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[4,5,6,7],[4,5,6,7],[4,5,6,7],[4,5,6,7]]
dirs = config.cla
answers = [] 
for i in range(len(dirs)) :
    ans = []
    ans.append(i)
    answers.append(ans)
 
for i in range(len(dirs)) :
    
    st = time.time()
    labels = predictor.predict_by_dir(model, root +'/' + dirs[i])
    print (labels) 
    acc = 0 
    for l in labels :
        if (l in answers[i]) :
            acc += 1 
    ar = float(acc) / len(labels)
    et = time.time()
    print ('directory:',root +'/' + dirs[i])
    print ('time elapse:', et - st)
    print ('acc/sample', acc, len(labels)) 
    print ('accuracy ratio:',ar)   

     
