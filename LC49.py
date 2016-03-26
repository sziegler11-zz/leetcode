class Solution(object):
    
    def toList(w1):
        l = [c for c in w1]
        l.sort()
        return l
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hasher = {}
        for s in strs:
            hasher[toList(s)] = []
        for s in strs:
            hasher[toList(s)].append(s)
            
        L=[]
        
        
