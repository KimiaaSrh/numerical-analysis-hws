import numpy as np
import math
# soorat=np.log(1.9)-np.log(1.8)
# print(float(soorat/0.1))
# print(float(float(0.1)/float(2*(1.8**2))))


def f(val):
    return float(val*math.exp(val))

# end-point 3 points:
def getFprimeThreeEndpoint(x0,h,fx0,fx1,fx2):
    part1=float(float(1.0)/float(2*h))*float(-3*fx0+4*fx1-fx2)
    # print(part1)
    part2=max(float(float(h**2)/float(3.0))*float(math.exp(x0)*(3+x0) ), float(float(h**2)/float(3.0))*float(math.exp(x0+h)*(3+x0+h) ) )
    # print(part2)
    print(part1+part2)

# mid-point 3 points:
def getFprimeThreeMidpoint(x0,h):
    part1=float(float(1.0)/float(2*h))*float(f(x0+h)-f(x0-h))
    # print(part1)
    # part2=max(float(float(h**2)/float(6.0))*float(math.exp(x0-h)*(3+x0-h) ), float(float(h**2)/float(6.0))*float(math.exp(x0+h)*(3+x0+h) ) )
    # print(part2)
    print(part1)

# mid-point 5 points:
def getFprimeFiveMidpoint(x0,h):
    part1=float(float(1.0)/float(12*h))*float(f(x0-2*h)-8*f(x0-h)+8*f(x0+h)-f(x0+2*h))
    # print(part1)
    # part2=max(float(float(h**3)/float(30.0))*float(math.exp(x0-h)*(3+x0-h) ), float(float(h**2)/float(6.0))*float(math.exp(x0+h)*(3+x0+h) ) )
    # print(part2)
    return (part1)

# end-point 5 points:
def getFprimeFiveEndpoint(x0,h):
    part1=float(float(1.0)/float(12*h))*float((-25)*f(x0)+48*f(x0+h)-36*f(x0+2*h)+16*f(x0+3*h)-3*f(x0+4*h))
    # print(part1)
    # part2=max(float(float(h**3)/float(30.0))*float(math.exp(x0-h)*(3+x0-h) ), float(float(h**2)/float(6.0))*float(math.exp(x0+h)*(3+x0+h) ) )
    # print(part2)
    print(part1)

# def secondDerivativeMidpoint():



# getFprimeThreeEndpoint(2,0.1,14.778112,17.148957,19.855030)
# getFprimeThreeMidpoint(2,0.1)
# getFprimeFiveMidpoint(2,0.1)
# print(getFprimeFiveMidpoint(2,0.2))
# getFprimeFiveMidpoint(2,0.05)
print(2*getFprimeFiveMidpoint(2,0.1)-getFprimeFiveMidpoint(2,0.2))
# getFprimeFiveEndpoint()
