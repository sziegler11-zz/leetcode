def reversewords(st):
    a=[]
    c=False
    j=len(st)-1
    while j > -1:
        if not st[j].isspace():
            t=""
            while j > -1 and not st[j].isspace():
                t=st[j] + t
                j-=1
            a.append(t)
        else:
            j-=1
    if len(a) == 0:
        return ""
    newst=""
    for i in range(len(a)-1):
        newst = newst + a[i] + " "
    newst = newst + a[len(a)-1]
    return newst
                
                
