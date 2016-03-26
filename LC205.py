def funny(s,t):
        if len(s) != len(t):
            return False
        elif len(s) == 0:
            return True
        d={}
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
