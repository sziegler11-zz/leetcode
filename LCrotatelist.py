def rotate(nums, k):
        n = len(nums)
        
        k = k%n
        
        for i in range(k):
            u = nums.pop()
            nums.insert(0,u)
        
