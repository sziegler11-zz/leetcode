def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        elif amount < 0 or len(coins)==0:
            return -1

        
        a=[]
        for i in range(len(coins)):
            a.append(coinChange(coins,amount-coins[i]))
        
        mi = max(a)
        
        for j in range(len(a)):
            if a[j] < mi:
                mi = a[j]
        
        if mi == -1:
            return -1
        else:
            return mi+1
            
