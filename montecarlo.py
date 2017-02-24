#monte carlo simulation calculation of PI

import random
import math
import numpy

#generate spots of x and y
xlist=[]
ylist=[]
cycle=10000
for i in range(0,cycle):
    xlist.append(numpy.random.rand())
    ylist.append(random.random())



#counting how many sopts in the circle
incount=0;
outcount=0;

for i in range(0,cycle):
    dist=xlist[i]*xlist[i]+ylist[i]*ylist[i]
    if dist<1:
        incount +=1
    else:
        outcount +=1

print incount
print outcount

#calculation of PI

pi=float(incount)/outcount
print pi
