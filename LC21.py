class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeLists(l1,l2):
    if l1 == None:
            return l2
    elif l2 == None:
            return l1
      
    if l1.val < l2.val:
            u = l1
            l1 = l1.next
    else:
            u = l2
            l2 = l2.next
    v = u    
        
    while l1 != None and l2 != None:
        if l1.val < l2.val:
                v.next = l1
                l1 = l1.next
        else:
                v.next = l2
                l2 = l2.next
        v = v.next
        
    if l1 == None and l2 != None:
            while l2 != None:
                v.next = l2
                l2 = l2.next
                v = v.next
    elif l1 != None and l2 == None:
             while l1 != None:
                v.next = l1
                l1 = l1.next
                v = v.next
    return u

def tester(r1,r2):
    u1 = ListNode(r1[0])
    u2 = ListNode(r2[0])
    v = u1
    w = u2

    for i in range(1,len(r1)):
        v.next = ListNode(r1[i])
        v = v.next
    for j in range(1,len(r2)):
        w.next = ListNode(r2[j])
        w = w.next
    q = mergeLists(u1,u2)
    arr=[]
    while q != None:
        arr.append(q.val)
        q=q.next
    print arr
        
