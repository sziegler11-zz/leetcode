def mintot(triangle):
    n = len(triangle)
    if n == 1:
        return triangle[0][0]
    if n == 2:
        arr = triangle[1]
        if arr[0] < arr[1]:
            return triangle[0][0] + arr[0]
        else:
            return triangle[0][0] + arr[1]
    elif n > 2:
        bob1 = []
        bob2 = []
        for i in range(1,n):
            u=[]
            v=[]
            for j in range(i):
                u.append(triangle[i][j])
                v.append(triangle[i][j+1])
            bob1.append(u)
            bob2.append(v)
        
        
        t1=mintot(bob1)
        t2=mintot(bob2)
        if t1 < t2:
            return triangle[0][0] + t1
        else:
            return triangle[0][0] + t2
