import math
x=0
i=0
while(i<55):
    print(str(i))
    y=x
    print(x)
    # x=float(2-math.exp(x)+x**2 )/3.0
    # x=(float(5.0/x**2)+2)
    # x=math.sqrt((float(math.exp( x ))/3.0))
    # x=float(5.0 ** (-x))
    # x=float(6.0 ** (-x))
    x=float(0.5)*(math.sin(x)+math.cos(x))
    print("error : "+str(float(x-y)))
    print("------------------")
    i=i+1

# other functions:

#x=x**3-x-5
