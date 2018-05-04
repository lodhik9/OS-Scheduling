import random
import sys
import os

class time():
    def __init__(self, arr, bust,pid,pri):
        self.arr = arr
        self.bust = bust
        self.pid=pid
        self.pri=pri

def sortlist(x,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if x[j].pri < x[i].pri:
                x[j], x[i] = x[i], x[j]

no_of_process=(input("Input No. of process="))

totalT=0
total2=0

x=[]
for i in range(0,no_of_process):
    print("Enter No of Process " + str (i + 1))
    p = input ("Enter Pid")
    a=input("Enter arrT")
    b=input("Enter bustT")
    c=input("Enter priority")

    x.append(time(a ,b ,p,c))

print x
print x[0].arr, x[0].bust
print x[1].arr, x[1].bust
sortlist(x,no_of_process)
for j in range(0,no_of_process):

    startT=totalT
    totalT=totalT+x[j].bust
    print("Starting at "+ str(startT)+ "Process no "+ str(x[j].pid)+ " ending at "+ str(totalT))
