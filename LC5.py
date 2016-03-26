def longpal(s):
    n = len(s)
    maxpal = ''

    for k in range(1,n+1):
        for i in range(0,n+1-k):
            j=0
            while s[i+j] == s[i+k-1-j] and j < k/2:
                j+=1
            if j == k/2:
                maxpal = s[i:i+k]

    return maxpal
            
