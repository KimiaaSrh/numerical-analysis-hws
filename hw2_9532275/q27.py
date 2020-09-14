x=0.01
i=0
while(i<12):
    print(str(i))
    y=x
    print(x)
    x=float(x)-(float(1000.0*(1.0-float((1.0+x)**(-360.0))))-float(135000.0*x))/float((360000.0)*(float((1.0+x)**(-361.0)))-135000.0)
    print("error : "+str(x-y))
    print("------------------")
    i=i+1
