#coding=utf-8  
'''
Created on 2017年4月1日
@author: caixq
'''
import config
import file_process

#To-Do dynamic cls based on directory names
cls = config.cla 

rawdir ='D:/ImageClassification/gallary/appliance'
traindir= 'D:/workspace/ImgClf/data/train'
validir = 'D:/workspace/ImgClf/data/validation'

file_process.PrepareDataSet(rawdir,cls,traindir,validir)
