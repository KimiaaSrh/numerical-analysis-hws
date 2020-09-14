import math
import numpy as np

# print(math.cos(0.25)**2*0.5)

# print((-0.5)*np.log(0.5)*0.25)

# print((float(0.55)/float(2))*(math.sin(1.3)**2-2*(1.3)*math.sin(1.3)+2+math.sin(0.75)**2-2*0.75*math.sin(0.75)))

p1=math.exp(1)+1
p2=np.log(math.exp(1)+1)
p3=float(1)/float(p1*p2)
p4=np.log(math.exp(1))*math.exp(1)
p5=float(1)/float(p4)
print(0.5*(p3+p5))
