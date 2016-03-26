def combinationSum3(k, n, nums):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 1 and n in nums:
            return [[n]]
        elif k > 1:
            A = []
            B = []
            for i in range(len(nums)):
                A=A+(combinationSum3(k-1,n-nums[i],nums[i+1:]))
            for i in range(len(A)):
                if len(A[i]) == k-1:
                    B.append([n-sum(A[i])] + A[i])
            return B
        else:
            return []

combinationSum3(3,9,range(1,10))
