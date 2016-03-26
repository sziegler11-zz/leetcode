
def fun(A):
        while True:
            if len(A) ==1 or len(A) == 0:
                break
            if A[0] > A[1]:
                A.append(A[0])
                A = A[1:]
                break
            if A[0]==A[1]:
                A = A[1:]
            else:
                A.append(A[0])
                A = A[1:]
        return len(A)
            
