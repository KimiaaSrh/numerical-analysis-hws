import numpy
import math

def f(x):
    return math.exp(3*x)*math.sin(2*x)

def romberg( f, a, b, n ):
    r = numpy.array( [[0] * (n+1)] * (n+1), float )
    h = b - a
    r[0,0] = 0.5 * h * ( f( a ) + f( b ) )

    powerOf2 = 1
    for i in range( 1, n + 1 ):
        h = 0.5 * h

        sum = 0.0
        powerOf2 = 2 * powerOf2
        for k in range( 1, powerOf2, 2 ):
            sum = sum + f( a + k * h )

        r[i,0] = 0.5 * r[i-1,0] + sum * h

        powerOf4 = 1
        for j in range( 1, i + 1 ):
            powerOf4 = 4 * powerOf4
            r[i,j] = r[i,j-1] + ( r[i,j-1] - r[i-1,j-1] ) / ( powerOf4 - 1 )

    return r
print(romberg(f,0,float(math.pi)/4.0,4))
