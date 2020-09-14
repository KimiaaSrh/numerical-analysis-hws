import numpy as np
import math
# soorat=np.log(1.9)-np.log(1.8)
# print(float(soorat/0.1))
# print(float(float(0.1)/float(2*(1.8**2))))
def getFprime(fx0Plush,fx0,h):
    print (float(fx0Plush-fx0)/float(h))

getFprime(1.2625,1.0,0.2)
getFprime(1.6595,1.2625,0.2)
# getFprime(2.0421,2.0601,-0.1)
# getFprime(1.9507,2.0421,-0.1)
