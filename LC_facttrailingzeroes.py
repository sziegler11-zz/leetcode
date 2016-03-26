import math

def factcount(n):
    f = int(math.log(n,5))
    t = int(math.log(n,2))

    numfives = numtwos = 0

    if(f>0):
        for i in range(1,f+1):
            numfives += n/(5**i)

    if(t>0):
        for j in range(1,t+1):
            numtwos += n/(2**j)

    return min(numfives,numtwos)
    
        
