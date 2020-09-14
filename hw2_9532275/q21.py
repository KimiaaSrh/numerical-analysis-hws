import math
x=10
i=0
while(i<12):
    print(str(i))
    y=x
    print(x)
    x=float(x)-float((float(4.0*x**2.0))-float(math.exp( x ))-float(math.exp( -x )))/float((float(8.0*x))-float(math.exp( x ))+float(math.exp( -x )))
    print("error : "+str(x-y))
    print("------------------")
    i=i+1
