#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
#author:koalabear  
#email:koalabearguo@gmail.com  
import sys  
import urllib  
import os  
from shutil import copyfile  
  
syspath=os.environ['systemdrive']

HOSTS_URL='https://raw.githubusercontent.com/racaljk/hosts/master/hosts'  
  
LOCAL_HOSTS=syspath+'\\Windows\\System32\\drivers\\etc\\hosts'  
  
def update():  
    """update hosts from smarthost"""  
    # backup hosts file  
    # copyfile(LOCAL_HOSTS,'hosts.bak')  
    with open(LOCAL_HOSTS,'w') as hosts:  
       # �ַ���������ǰƽ̨ʹ�õ�����ֹ�������磬Windowsʹ��'\r\n'��Linuxʹ��'\n'��Macʹ��'\r'��  
        hosts.write(os.linesep)  
        for line in urllib.urlopen(HOSTS_URL):  
            hosts.write(line.strip()+os.linesep)  
	#print LOCAL_HOSTS
    print "google hosts update success!"  
  
if __name__ == '__main__':  
    if len(sys.argv)>1:  
        HOSTS_URL = sys.argv[1]  
    update()  