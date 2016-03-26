def wordBreak(s, dict):
        if s == "":
            return True
        newdict = set([])
        for word in dict:
            i=0
            while i < len(word):
                if i > (len(s)-1) or s[i] != word[i]:
                    break
                else:
                    i+= 1
                    
            if i == len(word):
                newdict.add(word)
        
        t = False
        for word in newdict:
            t = t or wordBreak(s[len(word):],dict)
        return t
