#coding=utf-8  
'''
Created on 2017年3月20日
@author: caixq
'''

# issues : 
# 1. cannot read image URLs from Bing Search
# 2. firewall in China (google, yahoo)

from pisces import Pisces

if __name__ == '__main__':
   
    # ['sogou','baidu','360','bing','google','yahoo']
    # ['firefox', 'chrome', 'ie', 'opera', 'safari']
    
    search = '360'
    client = Pisces(quiet=False, close=True, browser='firefox') 
    
    cla = ['feather','coat','sweater','long','short','vest','swimsuit']
    keywords = ['羽绒外套模特','外套模特','毛衣模特','毛衣模特','短袖模特','女背心模特','泳装模特']
    
    for i in xrange(len(cla)):
        output_dir = '..\\crawler_unclear_data\\' + search + '\\' + cla[i]  #windows directory
        client.download_by_word(keywords, search, output_dir, image_count=3000)
    
    
    '''
    output_dir = '..\\crawler_data\\' + search + '\\feather'  #windows directory
    client.download_by_word('羽绒外套模特', search, output_dir, image_count=3000)
    
    output_dir = '..\\crawler_data\\' + search + '\\coat'  #windows directory
    client.download_by_word('外套模特', search, output_dir, image_count=3000)
            
    output_dir = '..\\crawler_data\\' + search + '\\sweater'  #windows directory
    client.download_by_word('毛衣模特', search, output_dir, image_count=3000)
    
    output_dir = '..\\crawler_data\\' + search + '\\long'  #windows directory
    client.download_by_word('长袖模特', search, output_dir, image_count=3000)
    
    output_dir = '..\\crawler_data\\' + search + '\\short'  #windows directory
    client.download_by_word('短袖模特', search, output_dir, image_count=3000)
    
    output_dir = '..\\crawler_data\\' + search + '\\vest'  #windows directory
    client.download_by_word('女背心模特', search, output_dir, image_count=3000)
       
    output_dir = '..\\crawler_data\\' + search + '\\swimsuit'  #windows directory
    client.download_by_word('泳装模特', search, output_dir, image_count=3000)
    
    '''
    #output_dir = '..\\crawler_data\\' + search + '\\naked'  #windows directory
    #client.download_by_word('三点全露', search, output_dir, image_count=3000)
    