import math
def f(x):
    return math.cos(x)
def lag2(x,x0,x1):
    fx0=1
    fx1=1.64872
    fx2=2.71828
    fx3=4.48169
    L0=float(x-x1)/float(x0-x1)
    L1=float(x-x0)/float(x1-x0)
    print(L0)
    print(L1)
    return fx0*L0+fx1*L1
def lag3(x,x0,x1,x2):
    fx0=1
    fx1=1.64872
    fx2=2.71828
    fx3=4.48169
    L0=(float(x-x1)/float(x0-x1))*(float(x-x2)/float(x0-x2))
    L1=(float(x-x0)/float(x1-x0))*(float(x-x2)/float(x1-x2))
    L2=(float(x-x0)/float(x2-x0))*(float(x-x1)/float(x2-x1))
    print(L0)
    print(L1)
    print(L2)
    return fx0*L0+fx1*L1+fx2*L2
def lag4(x,x0,x1,x2,x3):
    fx0=1
    fx1=1.64872
    fx2=2.71828
    fx3=4.48169
    L0=(float(x-x1)/float(x0-x1))*(float(x-x2)/float(x0-x2))*(float(x-x3)/float(x0-x3))
    L1=(float(x-x0)/float(x1-x0))*(float(x-x2)/float(x1-x2))*(float(x-x3)/float(x1-x3))
    L2=(float(x-x0)/float(x2-x0))*(float(x-x1)/float(x2-x1))*(float(x-x3)/float(x2-x3))
    L3=(float(x-x0)/float(x3-x0))*(float(x-x1)/float(x3-x1))*(float(x-x2)/float(x3-x2))
    print(L0)
    print(L1)
    print(L2)
    print(L3)
    return fx0*L0+fx1*L1+fx2*L2+fx3*L3

# x=0.45
# x0 = 0
# x1 = 0.6
# x2 = 0.9
x=0.43
x0=0
x1=0.25
x2=0.5
x3=0.75
# print('lag2')
# print(lag2(x,x0,x1))
# print()
# print('lag3')
# print(lag3(x,x0,x1,x2))
# print()
print('lag4')
print(lag4(x,x0,x1,x2,x3))
