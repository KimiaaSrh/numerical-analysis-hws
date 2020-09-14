import numpy as np
import math
def f(t,y):
    # p1=float(y)/float(t)
    # p2=p1**2
    # return p1+p2+1
    # return float(2-2*t*y)/float(t**2+1)
    return float(y**2)/float(1+t)


def y(t):
    # return float(t)/float(1+np.log(t))
    # return t*math.tan(np.log(t))
    # return float(2*t+1)/float(t**2+1)
    return float(-1)/float(np.log(t+1))

def runge_ka(a,b,h,alpha):
    n=float(b-a)/float(h)
    t=a
    w=alpha
    i=1
    while(i<=n+1):
        print('------i------',i)
        print('t    ',t)
        print('w    ',w)
        print('y    ',y(t))
        print()
        K1 = h*f (t, w)
        K2 = h*f (t + float(h)/2.0,w + float(K1)/2.0)
        K3 = h*f (t + float(h)/2.0,w + float(K2)/2.0)
        K4 = h*f (t + h,w + K3)
        print('k1 is ',K1)
        print('k2 is ',K2)
        print('k3 is ',K3)
        print('k4 is ',K4)
        w = w +float (K1 + 2*K2 + 2*K3 + K4)/6.0
        t = a + i*h
        i+=1

# runge_ka(1,2,0.1,1)
# runge_ka(1,3,0.2,0)
# runge_ka(0,1,0.1,1)
runge_ka(1,2,0.1,float(-1)/float(np.log(2)))
