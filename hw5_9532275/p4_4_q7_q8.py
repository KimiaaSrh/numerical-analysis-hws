import math
import numpy as np

def f(x):
    # return x**2*np.log(x**2+1)
    return x**2*math.exp(-x**2)

# fs=f(0)+2*(f(0.25)+f(0.5)+f(0.75)+f(1)+f(1.25)+f(1.5)+f(1.75))+f(2)
# print(float(fs*(0.25))/2.0)

def simpson(b,a,h,n):
    xi0=f(a)+f(b)
    xi1=0
    xi2=0
    i=1
    while(i<n):
        x=a+i*h
        if(i%2==0):
            xi2=xi2+f(x)
        else:
            xi1=xi1+f(x)
        i+=1
    xi=h*float(xi0+2*xi2+4*xi1)/float(3.0)
    return xi

# fs=f(0)+f(0.5)+f(1)+f(1.5)+f(2)
fs=f(0.25)+f(0.75)+f(1.25)+f(1.75)
print(fs*0.5)
