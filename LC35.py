def binins(A,target):
    m=0
    n=len(A)-1
    if len(A) == 0:
        return 0
    while m != n:
        l=(n+m)/2
        if A[l] == target:
            return l
        elif A[l] < target:
            m = l
        else:
            n = l

    if A[n] == target:
        return n
    elif A[n] < target:
        return n+1
    else:
        if n == 0:
            return 0
        else:
            return n-1
        
