def main():
    def relprime(a,b):
        c=0
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                c+=1
            if c>1:
                return (False)
        if c==1:
            return(True)            
    test=int(input())
    for i in range(test):

        res=[1]
        n=int(input())
        for i in range(2,n+1):
            c=0
            for j in range(1,i):
                if relprime(j,i):
                    c+=1
            res.append(c)    
        re=""
        for i in range(len(res)):
             re+=(str(res[i])+" ") 
        print(re)            
main()  
