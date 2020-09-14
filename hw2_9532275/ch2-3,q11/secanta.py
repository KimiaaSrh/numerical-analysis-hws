import math
i=2
p0=1
p1=2
q0=3 * p0 * math.exp(p0)
q1=3 * p1 * math.exp(p1)
print(q0)
print(q1)
while(i<20):
    p=p1 - float(q1*( p1 - p0))/float(q1 - q0)
    # if(p-p1>=10**(-4)):
    print("approx: ",str(p))
    print("error: "+str(p-p1))
    print(i)
    print("------------------------------")
    i+=1
    p0 = p1
    q0 = q1
    p1 = p
    q1 = 3 * p * math.exp(p)
