def countPrimes(n):
    if n < 3:
        return 0
    a=[0,0]+[1]*(n-2)
    c=0
    for i in range(2,n):
        if a[i]==1:
            k=2
            while k*i < n:
                a[k*i]=0
                k+=1
    return sum(a)
            
    
