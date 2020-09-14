import numpy as np


def getLowerTriangular(matrix,n,uniqueMatrix):
    w, h = n, 1;
    temp = [[0 for x in range(w)] for y in range(h)]
    temp2 = [[0 for x in range(w)] for y in range(h)]
    i=0
    alpha=0
    pivotingCount=0
    while(i<n-1):
        j=i+1
        while(j<=n-1):
            if(matrix[j][i]!=0.0 and  matrix[i][i]!=0.0):
                alpha=round(matrix[j][i],3)/round(matrix[i][i],3)
                k=0
                while(k<n):
                    temp[0][k]=round(alpha*(round(matrix[i][k],3)),3)
                    temp2[0][k]=round(alpha*(round(uniqueMatrix[i][k],3)),3)
                    k=k+1
                c=0
                while(c<n):
                    matrix[j][c]=round(matrix[j][c],3)-round(temp[0][c],3)
                    #khate baadi baraye be dast avordane inverse e
                    uniqueMatrix[j][c]=round(uniqueMatrix[j][c],3)-round(temp2[0][c],3)
                    c=c+1
            elif(matrix[i][i]==0):
                pivotingCount=pivotingCount+1
                counter=i+1
                while(counter<n):
                    if(matrix[counter][i]!=0):
                        counter2=0
                        while(counter2<n):
                            var=matrix[counter][counter2]
                            matrix[counter][counter2]=matrix[i][counter2]
                            matrix[i][counter2]=var
                            # 3 khate baadi baraye be dast avordane inverse e
                            var=uniqueMatrix[counter][counter2]
                            uniqueMatrix[counter][counter2]=uniqueMatrix[i][counter2]
                            uniqueMatrix[i][counter2]=var
                            counter2=counter2+1
                    counter=counter+1
                j=j-1
            j=j+1
        i=i+1
    return matrix , uniqueMatrix

def back_substitution(R,qty) :
    n = len(R)
    x = [[0 for x in range(1)] for y in range(n)]

    x[n-1] = qty[n-1]/R[n-1][n-1]
    for i in range(n-2, -1, -1):
        bb = 0
        for j in range (i+1, n):
            bb += R[i][j]*x[j]

        x[i] = (qty[i]-bb)/R[i][i]

    return x

# A=[[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
# y=[[4],[1],[-3],[4]]
# A=[[1, -1, 2, -1],[2 ,-2 ,3, -3],[1, 1, 1, 0],[1, -1, 4, 3]]
# y=[[-8],[-20],[-2],[4]]
A=[[0.03,58.9],[5.31,-6.1]]
y=[[59.2],[47]]
n=len(A)
I=[[0 for x in range(n)] for y in range(n)]
counter=0
while(counter<n):
    I[counter][counter]=1
    counter+=1
lowerA,unique=getLowerTriangular(A,n,I)
newY=np.dot(unique,y)
x=back_substitution(lowerA,newY)
# print(lowerA)
# print(newY)
print(x)
