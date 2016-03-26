def addBin(a,b,c):
        if b == "":
            if c ==0:
                return a
            else:
                return addBin("1",a,0)
        elif a == "":
            if c==0:
                return b
            else:
                return addBin("1",b,0)
        else:
            u = int(a[-1])
            v = int(b[-1])
            if u + v + c == 0:
                return addBin(a[:-1],b[:-1],c) + "0"
            elif u + v + c == 1:
                return addBin(a[:-1],b[:-1],0) + "1"
            elif u + v + c == 2:
                return addBin(a[:-1],b[:-1],1) + "0"
            elif u + v + c == 3:
                return addBin(a[:-1],b[:-1],1) + "1"
