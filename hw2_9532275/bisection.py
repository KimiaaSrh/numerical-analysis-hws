import math
def f(x):
    # return x**3+4*x**2-10
    return x**3-7*x**2+14*x-6
i=1
a=1
b=3.2
p=2
fa=f(a)
while(i<20):
    p = a + float(b - a)/2.0
    print('approximation: ',p)
    print(i)
    print('---------------------')
    i+=1
    fp=f(p)
    if(fa*fp>0):
        fa=fp
        a=p
    else:
        b=p
