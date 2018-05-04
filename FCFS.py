import random
import sys
import os

class time():
    def __init__(self, arr, bust,pid):
        self.arr = arr
        self.bust = bust
        self.pid=pid

def sortlist(x,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if x[j].arr < x[i].arr:
                x[j], x[i] = x[i], x[j]

no_of_process=(input("Input No. of process="))

totalT=0
total2=0

x=[]
for i in range(0,no_of_process):
    print("Enter No of Process " + str (i + 1))
    a=input("Enter arrT")
    b=input("Enter bustT")
    p=input("Enter Pid")
    x.append(time(a ,b ,p))

print x
print x[0].arr, x[0].bust
print x[1].arr, x[1].bust
sortlist(x,no_of_process)
for j in range(0,no_of_process):

    startT=totalT
    totalT=totalT+x[j].bust
    print("Starting at "+ str(startT)+ "Process no "+ str(x[j].pid)+ " ending at "+ str(totalT))
