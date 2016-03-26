def merge(A,m,B,n):
    for i in range(n):
        for j in range(m+i):
            if B[i] < A[j]:
                for k in range(m+i-1,j-1,-1):
                    A[k+1] = A[k]
                A[j]=B[i]
                print A
                break
                
                    
    
