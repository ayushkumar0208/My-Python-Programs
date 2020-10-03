i=1
a=1
while(i<=10):
    a=1
    c=0
    while(a<=i):
        if(i%a==0):
            c=c+1
            if(c<=2):
                 print(a)
        a=a+1
    i=i+1
    print()

            
