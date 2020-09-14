def euler(a,b,h,alpha):
    t=a
    w=alpha
    i=1
    n=float(b-a)/float(h)
    while(i<=n):
        t=a+i*h
        ti=a+(i+1)*h
        w=w+float(h)/float(2)*(f(t,w)+f(ti,w+h*f(t,w)))
        yi=y(t)
        print('-----i-----',i)
        print('t is   ,  ',t)
        print('w is   ,  ',w)
        print('y is   ,  ',yi)
        print()
        i+=1
