from copy import deepcopy
from math import sqrt
import numpy as np

def make_Identical_matrix(n):
    I=[]
    for i in range(n):
        mylist=[]
        for j in range(n):
            if(i==j):
                mylist.append(1)
            else:
                mylist.append(0)
        I.append(mylist)
    return I

def find_max_lower_row(A,k):
    m=abs(A[k][k])
    r=k
    for i in range(k+1,len(A)):
        if(abs(A[i][k])>m):
            m=abs(A[i][k])
            r=i
    if(m==0):
        return False
    else:
        return r

def exchange_rows(A,i,j):
    temp = A[i]
    A[i]=A[j]
    A[j]=temp
    return A
def upper_triangular(A,n,determinant_coeficient):


    for i in range(n-1) :

        print("--------------------------------------------------------")
        print("itrration :",i+1)

        row=find_max_lower_row(A,i)
        if(row):
            if(row!=i):
                A=exchange_rows(A,i,row)
                print("row exchange needed.",i,"and",row)
        else:
            print("find no non zero col. stoped.",i)
            break



        for j in range(i+1,n):
            alpha = -1 * (A[j][i]/A[i][i])
            for k in range(n+1):
                A[j][k] += alpha * A [i][k]
        for i in range(len(A)):
            for j in range(len(A[0])):
                print(str(A[i][j]) + "\t",end="")
            print()

    if(A[n-1][n-1]==0):
        print("find no non zero col. stoped.")
    return A,determinant_coeficient

def multiple_of_matrixes(A,B):
    if(len(A[0])==len(B)):
        C = [[0 for x in range(len(B[0]))] for y in range(len(A))]

        for i in range(len(A)): #row of A
                for k in range(len(B[0])): #column of B
                    temp=0
                    for j in range(len(A[0])): # column of A = row of B
                        temp+=A[i][j]*B[j][k]
                    C[i][k] = temp
        return C
    return False

def calculate_mines_of_matrixes(A,B):
    if(len(A)==len(B) and len(A[0])==len(B[0])):
        C = [[0 for x in range(len(A[0]))] for y in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j]=A[i][j]- B[i][j]
        return C
    return False

def back_sub(Ab):
    n = len(Ab)
    b=len(Ab[0])-1
    x = ["0"]*n
    for i in range(n-1, -1, -1):
        tmp = Ab[i][b]
        for j in range(n-1, i, -1):
            tmp -= x[j]*Ab[i][j]
        x[i] = tmp/Ab[i][i]

    return x



# Ab = [[1,-1,2,-1,-8],[2,-2,3,-3,-20],[1,1,1,0,-2],[1,-1,4,3,4]]
# Ab=[[30,591400,591700],[5.291,-6.130,46.78]]
Ab=[[0.03,58.9,59.2],[5.31,-6.10,47]]
# Ab=[[3.03,-12.1,14,-119],[-3.03,12.1,-7,120],[6.11,-14.2,21,-139]]
n=len(Ab)
determinant_coeficient_A = 1

print("upper triangular matrix :")

A_upper,determinant_coeficient_A = upper_triangular(Ab,n,determinant_coeficient_A)
x=back_sub(Ab)
print("--------------------------------------------------------")
print("x matrix :")
for i in range(n):
    print(x[i])
