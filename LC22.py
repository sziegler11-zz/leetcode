def genparen(n):
        if n == 1:
            return ['()']
        else:
            prev = genparen(n-1)
            new = []
            for s in prev:
                for i in range(len(s)):
                    for j in range(i,len(s)):
                        new.append(s[:i]+'('+s[i:j] + ')'+s[j:])
            return sorted(set(new)) #kind of a cheat :/
        
