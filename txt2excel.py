#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#-------------------------------------------------------------------------------
# Purpose:     txt转换成Excel
# use: python txt2excel.py out.txt ABC
#-------------------------------------------------------------------------------
import datetime
import time
import os
import xlwt #需要的模块
import sys

input_file = ""
recognizer_file = ""
out_file = ""

def txt2xls(input_file, recognizer_file, out_file):  #文本转换成xls的函数，filename 表示一个要被转换的txt文本，xlsname 表示转换后的文件名
    print('converting xls ... ')
    file1 = open(input_file)   #打开txt文本进行读取
    file2 = open(recognizer_file)

    
    x = 0                #在excel开始写的位置（y）
    y = 0                #在excel开始写的位置（x）
    xls = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True) #生成excel的方法，声明excel

    while True:  #循环，读取文本里面的所有内容
        line = file1.readline() #一行一行读取
        if not line:  #如果没有内容，则退出循环
            break
        for i in line.split('\t'):#读取出相应的内容写到x
            item=i.strip()
            sheet.write(x,y,item)
            # y += 1 #另起一列
        x += 1 #另起一行
        # y = 1  #初始成第一列
    # file1.close()
    x = 0
    while True:
        y = 1
        line2 = file2.readline()
        if not line2:
            break
        for j in line2.split('\t'):
            item2 = j.strip()
            sheet.write(x, y,item2)
            y += 1
        x += 1
    file2.close()
    xls.save(out_file) #保存

if __name__ == "__main__":
    print sys.argv
    if len(sys.argv) < 4:
        print "the param need tts_file, recognoizer_file, out_file"
    else:
        txt2xls(sys.argv[1], sys.argv[2], sys.argv[3])
