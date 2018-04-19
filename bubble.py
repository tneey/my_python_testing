import datetime
import urllib
import urllib2
import os
import random
import time
from multiprocessing import Pool
from multiprocessing import Process
starttime = datetime.datetime.now()

data = [21,3,4,7,8,12,3,11,36]

def bubble(data):
 n = len(data)
 for i in range(0,n):
  print data
  for j in range(0,8-i):
   if data[j] > data[j+1]:
    temp = data[j]
    data[j] = data[j+1]
    data[j+1] = temp

def insert(data):
 n = len(data)
 for i in range(1,n):
  print data
  for j in range(i,0,-1):
   if data[j-1] > data[j]:
    data[j],data[j-1] = data[j-1],data[j]
   else:
    break
 print data

def shell(data):
 n = len(data)
 d = n/2
 while d>0:
  for i in range(d,n,d):
   for j in range(i,0,-d):
    if data[j-d]>data[j]:
     data[j-d],data[j] = data[j],data[j-d]
    else:
	 break
  d = d/2
 print data
 
def partion(data,left,right):
 i = left
 j = right
 key = data[i]
 while (i < j):
  while (i < j) and (data[j] >= key):
   j = j -1 
  data[i] = data[j]
  while (i < j) and (data[i] < key):
   i = i + 1
  data[j] = data[i]
  data[i] = key
 return i
def quick(data,left,right):
 if left < right:
  p = partion(data,left,right)
  quick(data,left,p)
  quick(data,p+1,right)
  print data

def Bsearch(data,l,r,key):
 if l > r:
  return -1
 mid = l+(r-l)/2
 if key < data[mid]:
  return Bsearch(data, l ,mid - 1,key)
 if key > data[mid]:
  return Bsearch(data,mid + 1, r ,key)
 return mid

def binary_search(arr,start,end,hkey):
	if start > end:
		return -1
	mid = start + (end - start) / 2
	if arr[mid] > hkey:
		return binary_search(arr, start, mid - 1, hkey)
	if arr[mid] < hkey:
		return binary_search(arr, mid + 1, end, hkey)
	return mid 

 
def run_task(name):
 print 'Task %s (pid = %s) is running' %(name,os.getpid())
 time.sleep(random.random()*4)
 print 'Task %s end.'%name,
if __name__=='__main__':
 print 'Current process %s.' %os.getpid()
 p = Pool(processes = 3)
 for i in range(5):
  p.apply_async(run_task,args=(i,))																																																																																																																																																																																																																																																									
 print 'Waiting for all subprocesses done.......'
 p.close()
 p.join()
 print 'All subprocesses done.......'

endtime = datetime.datetime.now()
print (endtime - starttime)


















   