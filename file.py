#coding:utf-8
import os
def dirlist(path):
    filelist=os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        print filepath

dirlist('D:\\Python27\\test')

for path,d,filelist in os.walk('D:\\Python27\\test'):
    print path,d,filelist
    for filename in filelist:
        print os.path.join(path,filename)

        
    
