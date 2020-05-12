'''parallel rpm collection using multiprocessing library

Vivek M N 23082019
'''

import serial
import time
import multiprocessing

ser=serial.Serial('COM7',9600)
ser1=serial.Serial('COM11',9600)

time.sleep(10)

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
    s=ser.readline()
    a=s.decode('utf-8')
    print(a)
    print("hello")

def fun2():
    s1=ser1.readline()
    a=s1.decode('utf-8')
    print(a)
    print("world")



if __name__ == '__main__':
    print (__name__)
    proc = []
    print (proc)
    for fn in (fun1,fun2):
        p=multiprocessing.Process(target=fn)
        p.start()
        proc.append(p)
    print(proc)
    for p in proc:
        p.join()

time.sleep(100)
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
