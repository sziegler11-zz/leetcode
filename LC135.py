def candyHelp(ratings,l,r):
        if len(ratings)==1:
            return [max(l,r)]
        elif len(ratings) ==2:
            if ratings[0]<ratings[1]:
                if l < r:
                    return [l,r]
                else:
                    return [l,l+1]
            elif ratings[0] > ratings[1]:
                if l > r:
                    return [l,r]
                else:
                    return [r+1,r]
            else:
                return [l,r]
        if ratings[0] < ratings[1] and ratings[-1] < ratings[-2]:
            a = candyHelp(ratings[1:-1],l+1,r+1)
            return [l] + a + [r]
        elif ratings[0] < ratings[1] and ratings[-1] == ratings[-2]:
            a = candyHelp(ratings[1:-1],l+1,1)
            return [l] + a + [r]
        elif ratings[0] < ratings[1] and ratings[-1] > ratings[-2]:
            a = candyHelp(ratings[1:-1],l+1,1)
            return [l] + a + [max(r,a[-1]+1)]
        elif ratings[0] == ratings[1] and ratings[-1] < ratings[-2]:
            a = candyHelp(ratings[1:-1],1,r+1)
            return [l] + a + [r]
        elif ratings[0] == ratings[1] and ratings[-1] == ratings[-2]:
            a = candyHelp(ratings[1:-1],1,1)
            return [l] + a + [r]
        elif ratings[0] == ratings[1] and ratings[-1] > ratings[-2]:
            a = candyHelp(ratings[1:-1],1,1)
            return [l] + a + [max(r,a[-1]+1)]
        elif ratings[0] > ratings[1] and ratings[-1] < ratings[-2]:
            a = candyHelp(ratings[1:-1],1,r+1)
            return [max(l,a[0]+1)] + a + [r]
        elif ratings[0] > ratings[1] and ratings[-1] == ratings[-2]:
            a = candyHelp(ratings[1:-1],1,1)
            return [max(l,a[0]+1)] + a + [r]
        elif ratings[0] > ratings[1] and ratings[-1] > ratings[-2]:
            a = candyHelp(ratings[1:-1],1,1)
            return [max(l,a[0]+1)] + a + [max(r,a[-1]+1)]
