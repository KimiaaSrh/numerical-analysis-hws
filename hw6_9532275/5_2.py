import numpy as np
import math
def f(t,y):
    # return y-t**2+1
    # p1=float(y)/float(t)
    # p2=p1**2
    p1=-(y+1)*(y+3)
    # return p1-p2
    return p1

def y(t):
    # return -float(np.log(abs(float(t)/float(y)-1)))/float(t)
    # return float(t)/float(1+np.log(t))
    return -3+float(2)/float(1+math.exp(-2*t))
def euler(a,b,h,alpha):
    t=a
    w=alpha
    i=1
    n=float(b-a)/float(h)
    while(i<=n):
        w=w+h*f(t,w)
        t=a+i*h
        yi=y(t)
        print('-----i-----',i)
        print('t is   ,  ',t)
        print('w is   ,  ',w)
        print('y is   ,  ',yi)
        print()
        i+=1

# euler(0,2,0.2,0.5)
# euler(1,1.5,0.05,1)
# euler(0,2,0.2,-2)
# print(y(1.78))
# print(y(1.93))
# print(y(1.78))
# euler(1.78,2,0.03,y(1.78))
x0=1.8
x1=2
x=1.93
y0=-1.0299539
y1=-1.01815183
sag=float(y0*(x1-x)+y1*(x-x0))/float(x1-x0)
print(y(1.93))
print('y        ',sag)
