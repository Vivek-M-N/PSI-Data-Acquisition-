'''parallel rpm using threading library and xlwt for data logging in spreadsheet

Vivek M N 29082019
'''

import serial
import time
import threading
import xlwt 
from xlwt import Workbook 

filename = 'tacho_28032019.xls'
  
# Workbook is created 
wb1 = xlwt.Workbook()
wb2 = xlwt.Workbook()
  
# add_sheet is used to create sheet. 



#f1=open('primary.xls','a')
#f2=open('secondary.xls','a')

ser=serial.Serial('COM7',9600)
ser1=serial.Serial('COM11',9600)

def runparallel(*fns):
    #function to parallel
    if __name__ == '__main__':
        proc = []
        for fn in fns:
            p=Process(target=fn,args=(d,2))
            p.start()
            proc.append(p)
        for p in proc:
            p.join()

def func1(q):
    q.put("hello")
    q.put(-1)

def func2(q):
    q.put('world')
    q.put(-1)

def fun1():
    sheet1 = wb1.add_sheet('Pri')
    n=0
    while True:
        s=ser.readline()
        a=s.decode('utf-8')
        print(a)
        sheet1.write(n,0,a)
        n+=1
        
    #print("hello")

def fun2():
    sheet2 = wb2.add_sheet('Sec')
    n=0
    while True:
        s1=ser1.readline()
        a=s1.decode('utf-8')
        print(a)
        sheet1.write(n,1,a)
        n+=1
    #print("world")



if __name__ == '__main__':
    print (__name__)
    proc = []
    print (proc)
    for fn in (fun1,fun2):
        p=threading.Thread(target=fn)
        p.start()
        proc.append(p)
    print(proc)
    for p in proc:
        p.join()


wb1.save(filename)
wb2.save(filename)
'''if __name__ == '__main__':
    print('Now in the main code. Process name is:', __name__)
    q = multiprocessing.Queue()
    for f in (func1,func2):
        p = multiprocessing.Process(target=f, args=(q))
        p.start()

        while True:
            nq = q.get()
            print('Message is:', nq)
            if nq == -1:
                break

        print('Done')
    p.join()'''
