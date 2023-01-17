# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:23:09 2022

@author: M01
"""

import zipfile

'''
基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
mode：可選 r,w,a 代表不同的打開文件的方式；r 只讀；w 重寫；a 添加
compression：指出這個 zipfile 用什麼壓縮方法，默認是 ZIP_STORED，另一種選擇是 ZIP_DEFLATED；
allowZip64：bool型變量，當設置為True時可以創建大於 2G 的 zip 文件，默認值 True；

'''
path = r"______Your_ZIPfile.zi____"
folder_abs = r"./"
zip_file = zipfile.ZipFile(path)
zip_list = zip_file.namelist() # 得到壓縮包裡所有文件

for f in zip_list:
    zip_file.extract(f, folder_abs) # 循環解壓文件到指定目錄
 
zip_file.close() # 關閉文件，必須有，釋放內存
