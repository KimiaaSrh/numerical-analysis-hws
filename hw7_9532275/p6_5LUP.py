import numpy as np

def getLowerTriangular(matrix,n,uniqueMatrix,uniqueMatrix2):
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
                alpha=float(matrix[j][i])/float(matrix[i][i])
                uniqueMatrix[j][i]=alpha
                k=0
                while(k<n):
                    temp[0][k]=float(alpha*(float(matrix[i][k])))
                    k=k+1
                c=0
                while(c<n):
                    matrix[j][c]=float(matrix[j][c])-float(temp[0][c])
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
                            var=uniqueMatrix2[counter][counter2]
                            uniqueMatrix2[counter][counter2]=uniqueMatrix2[i][counter2]
                            uniqueMatrix2[i][counter2]=var
                            counter2=counter2+1
                    counter=counter+1
                j=j-1
            j=j+1
        i=i+1
    return matrix , uniqueMatrix ,uniqueMatrix2
def getTranspose(Q):
    numrows = len(Q)
    numcols = len(Q[0])
    QTranspose=[[0 for x in range(numrows)] for y in range(numcols)]
    counter=0
    while(counter<numrows):
        counter2=0
        while(counter2<numcols):
            QTranspose[counter2][counter]=Q[counter][counter2]
            counter2+=1
        counter+=1
    return QTranspose

# A=[[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
# A=[[1, -1, 2, -1],[2 ,-2 ,3, -3],[1, 1, 1, 0],[1, -1, 4, 3]]
# A=[[0.03,58.9],[5.31,-6.1]]
# A=[[1,-1,0],[2,2,3],[-1,3,2]]
# A=[[2,1,0,0],[-1,3,3,0],[2,-2,1,4],[-2,2,2,5]]
# A = [[0,0,-1,1],[1,1,-1,2],[-1,-1,2,0],[1,2,0,2]]
# A=[[0,2,3],[1,1,-1],[0,-1,1]]
# A=[[2,-1,1],[3,3,9],[3,3,5]]
# A=[[1,2,-1],[1,2,3],[2,-1,4]]
# A=[[1,-2,3,0],[3,-6,9,3],[2,1,4,1],[1,-2,2,-2]]

n=len(A)
# n=4
I=[[0 for x in range(n)] for y in range(n)]
I2=[[0 for x in range(n)] for y in range(n)]
counter=0
while(counter<n):
    I[counter][counter]=1
    I2[counter][counter]=1
    counter+=1
U,L,P=getLowerTriangular(A,n,I,I2)
print('---Upper---')
print(U)
print('---Lower---')
print(L)
print('---P---')
print(P)
PTRansLres=np.dot(getTranspose(P),L)
LUPres=np.dot(PTRansLres,U)
print('---resulted A---')
print(LUPres)
