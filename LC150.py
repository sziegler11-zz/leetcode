def percolate(toke, n):
        if len(toke[-1][1]) == 0:
            toke[-1][1].append(n)
        elif len(toke[-1][1]) == 1:
            m = toke[-1][1][0]
            o = toke[-1][0]
            if o == "+":
                c=m+n
            elif o == "-":
                c=m-n
            elif o == "/":
                c=m/n
            elif o == "*":
                c=m*n
            toke.pop()
            if len(toke) == 0:
                return c
            else:
                return percolate(toke,c)
