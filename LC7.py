def reverse(self, x):
        u = str(x)
        neg = False
        if u[0] == '-':
            neg == True
            u = u[1:]
        
        v=''
        
        for i in range(len(u)):
            v=v+u[len(u)-1-i]
        
        if neg == True:
            return int('-' + v)
        else:
            return int(v)
