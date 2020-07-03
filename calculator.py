class calculator:
    def add(self,argv):
        sum=0
        print_string=''
        for arg in argv:
            sum=sum+float(arg)
        for i in range(0,len(argv)):
            print_string=print_string+str(argv[i])
            if(i!=len(argv)-1):
                print_string=print_string+' + '
        print_string=print_string+' = '
        print_string=print_string+str(sum)
        return sum

    def subtract(self,argv):
        diff=float(argv[0])+float(argv[0])
        print_string=''
        for arg in argv:
            diff=diff-float(arg)
        for i in range(0,len(argv)):
            print_string=print_string+str(argv[i])
            if(i!=len(argv)-1):
                print_string=print_string+' - '
        print_string=print_string+' = '
        print_string=print_string+str(diff)
        return diff

    def multiply(self,argv):
        product=1
        print_string=''
        for arg in argv:
            product=product*float(arg)
        for i in range(0,len(argv)):
            print_string=print_string+str(argv[i])
            if(i!=len(argv)-1):
                print_string=print_string+' * '
        print_string=print_string+' = '
        print_string=print_string+str(product)
        return product

    def divide(self,argv):
        quotient=float(argv[0])*float(argv[0])
        print_string=''
        for arg in argv:
            quotient=float(quotient)/float(arg)
        for i in range(0,len(argv)):
            print_string=print_string+str(argv[i])
            if(i!=len(argv)-1):
                print_string=print_string+' / '
        print_string=print_string+' = '
        print_string=print_string+str(quotient)
        return quotient
#c=calculator()
#n1=445
#n2=202
#print_string=c.multiply(n1,n2)
#print(print_string)
