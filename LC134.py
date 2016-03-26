#since the solution is unique, the station "before" the solution
#must have had a greater cost than gas.


def gasloop(gas,cost):
##    n=len(gas)
##    for i in range(n):
##            j=i
##            c=gas[j]
##            d=cost[j]
##            if c >= d:
##                while c >= d:
##                    j=((j+1)%n)
##                    c+= gas[j]
##                    d+= cost[j]
##                    if j == i:
##                        return i
##    return -1
    n = len(gas)
    totgas = 0
    totcost = 0
    for i in range(n):
        totgas+= gas[i]
        totcost+= cost[i]
    if totgas < totcost:
        return -1

    
