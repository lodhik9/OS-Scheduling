import random
import sys
import os
from collections import deque

chart=[]
class process:
    def __init__(self, arr, bust, pid):
        self.arr = arr
        self.bust = bust
        self.pid = pid
def shiftCL(alist):
    temp = alist[0]
    for i in range(len(alist)-1):
        alist[i]=alist[i+1]
    alist[len(alist)-1]=temp
    return alist

def RR(tq,plist,n):
        global chart
        queue=[]
        time=0
        ap=0 #arrived process
        rp=0 #ready process
        done=0 #done process
        q=tq #time quantum
        start=0
        while(done<n):
            for i in range(ap,n):
                if time>=plist[i].arr:
                    queue.append(plist[i])
                    ap+=1
                    rp+=1
            if rp<1:
                chart.append(0)
                time+=1
                continue
            if start:
                queue=shiftCL(queue)
            if queue[0].bust>0:
                if queue[0].bust>q:
                    for j in range(time, time+q):
                        chart.append(queue[0].pid)
                    time+=q
                else:
                    for j in range(time, time+queue[0].bust):
                        chart.append(queue[0].pid)
                    time+=queue[0].bust
                    queue[0].bust=0
                    done+=1
                    rp-=1
                start=1

plist=[]
plist.append(process(1,0,5))
plist.append(process(2,1,3))
plist.append(process(3,3,6))
plist.append(process(4,5,1))
plist.append(process(5,6,4))

RR(3,plist,len(plist))
print chart
