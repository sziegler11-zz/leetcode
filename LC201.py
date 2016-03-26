def convtobin(n,l):
    a=[]
    c=n
    while c>0:
        a.append(c%2)
        c=c/2
    while len(a) < l:
        a.append(0)
    return a

def bitwisedig(m,n,k):
    r = m % (2**k)
    if r < 2**(k-1):
        return 0
    else:
        if n-m > 2**k -r-1:
            return 0
        else:
            return 1
    

def bitwiseand(m,n):
    a=[]
    k=0
    while 2**k <= n:
        a.append(bitwisedig(m,n,k+1))
        k+=1
    c=0
    for j in range(len(a)):
        c+= a[j]*(2**j)
    return c
    
    
