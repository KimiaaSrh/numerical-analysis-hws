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
            # print(matrix)
            if(matrix[j][i]!=0.0 and  matrix[i][i]!=0.0):
                alpha=float(matrix[j][i])/float(matrix[i][i])
                k=0
                while(k<n):
                    temp[0][k]=float(alpha*(float(matrix[i][k])))
                    temp2[0][k]=float(alpha*(float(uniqueMatrix[i][k])))
                    k=k+1
                c=0
                while(c<n):
                    matrix[j][c]=float(matrix[j][c])-float(temp[0][c])
                    #khate baadi baraye be dast avordane inverse e
                    uniqueMatrix[j][c]=float(uniqueMatrix[j][c])-float(temp2[0][c])
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
def inverse(matrix,n,uniqueMatrix):
    w, h = n, 1;
    temp = [[0 for x in range(w)] for y in range(h)]
    temp2 = [[0 for x in range(w)] for y in range(h)]
    i=n-1
    alpha=0
    while(i>=1):
        j=i-1
        while(j>=0):
            if(matrix[j][i]!=0.0 and  matrix[i][i]!=0.0):
                alpha=float(matrix[j][i])/float(matrix[i][i])
                k=0
                while(k<n):
                    temp[0][k]=float(alpha*(float(matrix[i][k])))
                    temp2[0][k]=float(alpha*(float(uniqueMatrix[i][k])))
                    k=k+1
                c=0
                while(c<n):
                    matrix[j][c]=float(matrix[j][c])-float(temp[0][c])
                    uniqueMatrix[j][c]=float(uniqueMatrix[j][c])-float(temp2[0][c])
                    c=c+1
            elif(matrix[i][i]==0):
                counter=i-1
                while(counter>=0):
                    if(matrix[counter][i]!=0):
                        counter2=0
                        while(counter2<n):
                            var=matrix[counter][counter2]
                            matrix[counter][counter2]=matrix[i][counter2]
                            matrix[i][counter2]=var
                            var=uniqueMatrix[counter][counter2]
                            uniqueMatrix[counter][counter2]=uniqueMatrix[i][counter2]
                            uniqueMatrix[i][counter2]=var
                            counter2=counter2+1
                        counter=counter-1
                j=j+1
            j=j-1
        i=i-1
    cc=0
    while(cc<n):
        if(matrix[cc][cc]!=1):
            xcount=0
            while(xcount<n):
                uniqueMatrix[cc][xcount]=float(uniqueMatrix[cc][xcount]*(float(1.0)/float(matrix[cc][cc])))
                xcount=xcount+1
        cc=cc+1
    return (uniqueMatrix)
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

n=4

# A=[[4,2,6],[3,0,7],[-2,-1,-3]]
# A=[[1,2,0],[2,1,-1],[3,1,1]]
# A=[[1,1,-1,1],[1,2,-4,-2],[2,1,1,5],[-1,0,-2,-4]]
A=[[4,0,0,0],[6,7,0,0],[9,11,1,0],[5,4,1,1]]
I=[[0 for x in range(n)] for y in range(n)]
counter=0
while(counter<n):
    I[counter][counter]=1
    counter+=1
lowerA,unique=getLowerTriangular(A,n,I)
invA=inverse(A,n,unique)
print(lowerA)
print(invA)
