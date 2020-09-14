import math

# def f(t,y,h):
#     p1=float(2)/float(t)*y+t**2*math.exp(t)
#     p2=float(h)/float(2)*(float(2)/float(t)-float(4)/float(t**3)*y+math.exp(t)*(2*t+t**2-2))
#     return p1+p2

def f(t,y,h):
    p1=float(2)/float(t)*y+t**2*math.exp(t)
    p2=float(h)/float(2)*(float(2)/float(t)-float(4)/float(t**3)*y+math.exp(t)*(2*t+t**2-2))
    p3=float(h**2)/float(6)*(float(-2)/float(t**2)+float(12)/float(t**4)*y-float(4)/float(t**3)+math.exp(t)*(4*t+t**2))
    p4=float(h**3)/float(24)*(float(4)/float(t**3)+float(-48)/float(t**5)*y+math.exp(t)*(6*t+t**2+4))
    return p1+p2+p3+p4

def y(t):
    return t**2 *(math.exp(t)-math.exp(1))

def euler(a,b,h,alpha):
    t=a
    w=alpha
    i=1
    n=float(b-a)/float(h)
    while(i<=n):
        w=w+h*f(t,w,h)
        t=a+i*h
        yi=y(t)
        print('-----i-----',i)
        print('t is   ,  ',t)
        print('w is   ,  ',w)
        print('y is   ,  ',yi)
        print()
        i+=1
euler(1,2,0.1,0)
# x0=1.9
# x1=2
# x=1.97
# y0=14.1526
# y1=18.46999
# sag=float(y0*(x1-x)+y1*(x-x0))/float(x1-x0)
# print(y(x))
# print('y      ',sag)
