import math
x=0.5
i=0
while(i<10):
    print(str(i))
    y=x
    print(x)
    x=float(x)-float(2.0*x+3.0*float(math.cos(x))-float(math.exp( x )))/float(2.0-3.0*float(math.sin(x))-float(math.exp( x )))
    print("error : "+str(x-y))
    print("------------------")
    i=i+1
