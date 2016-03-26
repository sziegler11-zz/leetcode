def subind(S,n):
    if n == 0:
        return [[]]
    elif n > 0:
        u = S.pop()
        M = subind(S,n-1)
        N = []
        for s in M:
            N.append(s+[u])
        return M+N

def subsets(S):
    n=len(S)
    return subind(S,n)
