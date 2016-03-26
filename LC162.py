def peaks(l):
    n=len(l)
    if n==1:
        return 0

    for i in range(n-1):
        if l[i] > l[i+1]:
            return i

    return n-1
    
