import math

def numSquares(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            sq = int(math.floor(math.sqrt(n)))
            min = n
            for k in range(1,sq+1):
                val = numSquares(n-k*k)
                if val < min:
                    min = val
            return 1 + min
                
        
