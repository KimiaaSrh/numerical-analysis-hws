import math
import numpy as np
def fPrime(x):
    # return (-4)*math.sin(2*x)-1
    return 2*x*np.log(x)+x

def getFprime(fx0Plush,fx0,h):
    return (float(fx0Plush-fx0)/float(h))

def getError(x,h):
    # return 4*h*math.cos(2*x)
    return float(2*np.log(x)+3)*(float(h)/float(2.0))

# print(fPrime(1))
# print(fPrime(1.2))
# print(fPrime(1.4))
# print(fPrime(1)-getFprime(1.2625,1.0,0.2))
# print(fPrime(1.2)-getFprime(1.6595,1.2625,0.2))
# print(fPrime(1.4)-getFprime(1.2625,1.6595,-0.2))
print(getError(1.2,0.2))
print(getError(1.4,0.2))
print(getError(1.4,-0.2))
