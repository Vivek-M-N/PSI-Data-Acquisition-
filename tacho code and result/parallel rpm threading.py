'''parallel test using threading library

Vivek M N 28082019'''

import serial
import time
import threading

ser=serial.Serial('COM7',9600)
ser1=serial.Serial('COM11',9600)

primary=open('prim.txt','a')
secondary=open('seco.txt','a')

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
    n=0
    while True:
        t=time.clock()
        s=ser.readline()
        a=s.decode('utf-8')
        print(t,a)
        primary.write(a)
        primary.write('\t')
        primary.write(str(t))
        
    #print("hello")

def fun2():
    n=0
    while True:
        s1=ser1.readline()
        a1=s1.decode('utf-8')
        print(a1)
        secondary.write(a1)
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

primary.close()
secondary.close()
