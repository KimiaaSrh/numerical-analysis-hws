x=0.01
i=0
while(i<10):
    print(str(i))
    y=x
    print(x)
    x=float(x)-(float(1500.0*(float((1.0+x)**(240.0))-1.0))-float(750000.0*x))/float((360000.0)*(float((1.0+x)**(239.0)))-750000.0)
    print("error : "+str(x-y))
    print("------------------")
    i=i+1
