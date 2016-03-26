def minrot(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return num[i+1]
    return num[0]
        
