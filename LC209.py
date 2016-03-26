#Trivial solution plus some memoization... still too slow

def findmin(s,A):
    n=len(A)
    B=[]
    for i in range(len(A)):
        B.append(A[i])
    for l in range(1,n+1):
        for i in range(len(B)):
            if B[i] >= s:
                return l
        B.pop()

        for i in range(len(B)):
            B[i] = B[i]+A[i+l]
        print B
    return 0

A=[2,3,1,4,3]
s=9

