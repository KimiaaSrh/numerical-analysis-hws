def sorat(n,k):
    m=n
    for i in range(1,k):
        m*=(n-i)
    return m
def func3(X,x1,x2,x3,x4,x5,fx1,fx2,fx3,fx4,fx5):

    fx1x2 = (fx2-fx1)/(x2-x1)
    fx2x3 = (fx3-fx2)/(x3-x2)
    fx3x4 = (fx4-fx3)/(x4-x3)
    fx4x5 = (fx5-fx4)/(x5-x4)

    fx1x2x3= (fx2x3-fx1x2)/(x3-x1)
    fx2x3x4= (fx3x4-fx2x3)/(x4-x2)
    fx3x4x5= (fx4x5-fx3x4)/(x5-x3)

    fx1x2x3x4 = (fx2x3x4-fx1x2x3)/(x4-x1)
    fx2x3x4x5 = (fx3x4x5-fx2x3x4)/(x5-x2)

    fx1x2x3x4x5 = (fx2x3x4x5-fx1x2x3x4)/(x5-x1)

    print('fx1x2',fx1x2)
    print('fx2x3',fx2x3)
    print('fx3x4',fx3x4)
    print('fx4x5',fx4x5)
    print()
    print('fx1x2x3',fx1x2x3)
    print('fx2x3x4',fx2x3x4)
    print('fx3x4x5',fx3x4x5)
    print()
    print('fx1x2x3x4',fx1x2x3x4)
    print('fx2x3x4x5',fx2x3x4x5)
    print()
    print('fx1x2x3x4x5',fx1x2x3x4x5)
    print()

 #   print(fx1+fx1x2*(X-x1))
 #   print(fx1+fx1x2*(X-x1)+fx1x2x3*(X-x1)*(X-x2))
 #   print(fx1+fx1x2*(X-x1)+fx1x2x3*(X-x1)*(X-x2)+fx1x2x3x4*(X-x1)*(X-x2)*(X-x3))
    h=x2-x1
    s=(X-x1)/h
    print('s for forward is',s)
    #print(fx1 + (sorat(s,1))* h**1 * fx1x2)
    #print(fx1 + (sorat(s,1))* h**1 * fx1x2 + (sorat(s,2))* h**2 *fx1x2x3)
    # forward esh doroste : ino kimia neveshte
    print(fx1 + (sorat(s,1))* h**1 * fx1x2 + (sorat(s,2))* h**2 *fx1x2x3 +(sorat(s,3))* h**3 *fx1x2x3x4 +(sorat(s,4))* h**4 *fx1x2x3x4x5)
    print()
    X=0.65
    s=(X-x5)/h
    print('s for backward is',s)
    #backward
    # print('hi')
    # print((s)* h**1 * fx4x5)
    # print((s*(s+1))* h**2 *fx3x4x5)
    # print((s*(s+1)*(s+2))* h**3 *fx2x3x4x5)
    # print((s*(s+1)*(s+2)*(s+3))* h**4 *fx1x2x3x4x5)
    # print('bye')
    print(fx5 + (s)* h**1 * fx4x5 + (s*(s+1))* h**2 *fx3x4x5 +(s*(s+1)*(s+2))* h**3 *fx2x3x4x5 +(s*(s+1)*(s+2)*(s+3))* h**4 *fx1x2x3x4x5)
    X=0.43
    s=(X-x3)/h
    print()
    print('strilings formula')
    print(fx3+((s*h)/2)*(fx2x3+fx3x4)+ s**2*h**2*fx2x3x4 + ((s*(s**2-1)*h**3)/2)*(fx1x2x3x4+fx2x3x4x5)+ s**2*(s**2-1)*h**4*fx1x2x3x4x5)


def func(X,x1,x2,x3,x4,x5,x6,fx1,fx2,fx3,fx4,fx5,fx6):

    fx1x2 = (fx2-fx1)/(x2-x1)
    fx2x3 = (fx3-fx2)/(x3-x2)
    fx3x4 = (fx4-fx3)/(x4-x3)
    fx4x5 = (fx5-fx4)/(x5-x4)
    fx5x6 = (fx6-fx5)/(x6-x5)


    fx1x2x3= (fx2x3-fx1x2)/(x3-x1)
    fx2x3x4= (fx3x4-fx2x3)/(x4-x2)
    fx3x4x5= (fx4x5-fx3x4)/(x5-x3)
    fx4x5x6= (fx5x6-fx4x5)/(x6-x4)

    fx1x2x3x4 = (fx2x3x4-fx1x2x3)/(x4-x1)
    fx2x3x4x5 = (fx3x4x5-fx2x3x4)/(x5-x2)
    fx3x4x5x6 = (fx4x5x6-fx3x4x5)/(x6-x3)

    fx1x2x3x4x5 = (fx2x3x4x5-fx1x2x3x4)/(x5-x1)
    fx2x3x4x5x6 = (fx3x4x5x6-fx2x3x4x5)/(x6-x2)

    fx1fx2x3x4x5x6=(fx2x3x4x5x6-fx1x2x3x4x5)/(x6-x1)

    print('fx1x2',fx1x2)
    print('fx2x3',fx2x3)
    print('fx3x4',fx3x4)
    print('fx4x5',fx4x5)
    print('fx5x6',fx5x6)
    print()
    print('fx1x2x3',fx1x2x3)
    print('fx2x3x4',fx2x3x4)
    print('fx3x4x5',fx3x4x5)
    print('fx4x5x6',fx4x5x6)
    print()
    print('fx1x2x3x4',fx1x2x3x4)
    print('fx2x3x4x5',fx2x3x4x5)
    print('fx3x4x5x6',fx3x4x5x6)
    print()
    print('fx1x2x3x4x5',fx1x2x3x4x5)
    print('fx2x3x4x5x6',fx2x3x4x5x6)
    print()
    print('fx1fx2x3x4x5x6',fx1fx2x3x4x5x6)

 #   print(fx1+fx1x2*(X-x1))
 #   print(fx1+fx1x2*(X-x1)+fx1x2x3*(X-x1)*(X-x2))
 #   print(fx1+fx1x2*(X-x1)+fx1x2x3*(X-x1)*(X-x2)+fx1x2x3x4*(X-x1)*(X-x2)*(X-x3))
    h=x2-x1
    s=(X-x1)/h
    # print('s for forward is',s)
    # #print(fx1 + (sorat(s,1))* h**1 * fx1x2)
    # #print(fx1 + (sorat(s,1))* h**1 * fx1x2 + (sorat(s,2))* h**2 *fx1x2x3)
    # # forward esh doroste : ino kimia neveshte
    # print(fx1 + (sorat(s,1))* h**1 * fx1x2 + (sorat(s,2))* h**2 *fx1x2x3 +(sorat(s,3))* h**3 *fx1x2x3x4 +(sorat(s,4))* h**4 *fx1x2x3x4x5)
    # print()
    # X=0.65
    # s=(X-x5)/h
    # print('s for backward is',s)
    # #backward
    # # print('hi')
    # # print((s)* h**1 * fx4x5)
    # # print((s*(s+1))* h**2 *fx3x4x5)
    # # print((s*(s+1)*(s+2))* h**3 *fx2x3x4x5)
    # # print((s*(s+1)*(s+2)*(s+3))* h**4 *fx1x2x3x4x5)
    # # print('bye')
    print(fx5 + (s)* h**1 * fx4x5 + (s*(s+1))* h**2 *fx3x4x5 +(s*(s+1)*(s+2))* h**3 *fx2x3x4x5 +(s*(s+1)*(s+2)*(s+3))* h**4 *fx1x2x3x4x5)
    # X=0.43
    # s=(X-x3)/h
    # print()
    # print('strilings formula')
    # print(fx3+((s*h)/2)*(fx2x3+fx3x4)+ s**2*h**2*fx2x3x4 + ((s*(s**2-1)*h**3)/2)*(fx1x2x3x4+fx2x3x4x5)+ s**2*(s**2-1)*h**4*fx1x2x3x4x5)

def func2(X,x1,x2,x3,x4,fx1,fx2,fx3,fx4):

    fx1x2 = (fx2-fx1)/(x2-x1)
    fx2x3 = (fx3-fx2)/(x3-x2)
    fx3x4 = (fx4-fx3)/(x4-x3)

    fx1x2x3= (fx2x3-fx1x2)/(x3-x1)
    fx2x3x4= (fx3x4-fx2x3)/(x4-x2)

    fx1x2x3x4 = (fx2x3x4-fx1x2x3)/(x4-x1)

    print('fx1x2',fx1x2)
    print('fx2x3',fx2x3)
    print('fx3x4',fx3x4)
    print()
    print('fx1x2x3',fx1x2x3)
    print('fx2x3x4',fx2x3x4)
    print()
    print('fx1x2x3x4',fx1x2x3x4)
    print()
    print()

    h=x2-x1
    s=(X-x1)/h
    print('s for forward is',s)
    print(fx1 + (sorat(s,1))* h**1 * fx1x2 + (sorat(s,2))* h**2 *fx1x2x3 +(sorat(s,3))* h**3 *fx1x2x3x4 )
    print()
    s=(X-x4)/h
    print('s for backward is',s)
    # print('hi')
    # print(fx4)
    # print((s)* h**1 * fx3x4 )
    # print((s*(s+1))* h**2 *fx2x3x4)
    # print((s*(s+1)*(s+2))* h**3 *fx1x2x3x4)
    # print('bye')
    print(fx4 + (s)* h**1 * fx3x4 + (s*(s+1))* h**2 *fx2x3x4 +(s*(s+1)*(s+2))* h**3 *fx1x2x3x4 )
    print()

func(1975,1950,1960,1970,1980,1990,2000,151.326,179.323,203.302,226.542,249.633,281.422)
# func(1.1,1,1.3,1.6,1.9,2.2,0.7651977,0.6200860,0.4554022,0.2818186,0.1103623)
# func2(0.43,0,0.25,0.5,0.75,1,1.64872,2.71828,4.48169)
# func2(0.18,0.1,0.2,0.3,0.4,-0.29004986,-0.56079734,-0.81401972,-1.0526302)
