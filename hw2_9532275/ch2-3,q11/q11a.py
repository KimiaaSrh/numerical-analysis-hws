import math
x=1.5
i=0
while(i<10):
    print(str(i))
    print(x)
    x=float(x)-float(x)/float(x+1)
    y=x
    print("error : "+str(y-x))
    print("------------------")
    i=i+1
