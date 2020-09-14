import numpy

# A=[[2,0,0],[1,1,2],[1,-1,4]]
# A=[[0,1],[-1,0]]
# A=[[2,-1],[-1,2]]
# A=[[2,1,0],[1,2,0],[0,0,3]]
# A=[[-1,2,0],[0,3,4],[0,0,7]]
# A=[[2,1,1],[2,3,2],[1,1,2]]
v=numpy.linalg.eig(A)

# A=[[1,0],[0.25,0.5]]
A=[[0.5,0],[16,0.5]]
A2=numpy.dot(A,A)
print('--a to power 2--')
print(A2)
A3=numpy.dot(A2,A)
print('--a to power 3--')
print(A3)
A4=numpy.dot(A2,A2)
print('--a to power 4--')
print(A4)

# print(v)
