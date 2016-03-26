def countAndSay(n):
    if n ==1:
        return "1"
    a=countAndSay(n-1)
    s=""
    num = a[0]
    c=1
    for i in range(1,len(a)):
        if num != a[i]:
            s = s+(str(c) + num)
            num=a[i]
            c=1
        else:
            c+=1
    s = s + (str(c) + num)
    return s
    
       
