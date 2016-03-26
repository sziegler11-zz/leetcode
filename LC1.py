def binsearch(l,m):
    r=len(l)-1
    w=0
    while True:
        i = (r+w)/2
        d= (r-w)/2
        if l[i] == m:
            return True
        elif r-w <= 1:
            if l[r] == m:
                return True
            else:
                return False
        elif l[i] < m:
            w+= d
        else:
            r-=d
        
            
            
    
    

def twosum(nums,target):
   new=sorted(nums)
   for i in range(len(new)-1):
       m=target-new[i]
       if binsearch(new[i+1:],m):
           break
   l=new[i]
   for j in range(len(nums)):
       if nums[j] == l:
           t1 = j+1
       if nums[j] == m:
           t2 = j+1
   return [t1,t2]
    
    
        
    
        
        
