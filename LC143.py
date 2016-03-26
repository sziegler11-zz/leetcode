class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


def reorder(head):
    l={}
    if head == None:
        return None
    i=0
    while True:
        l[i] = head
        i+=1
        head=head.next
        if head == None:
            break
    n=i-1
    if n == 0:
        return l[0]
    elif n%2 == 0:
        j=0
        while n > j:
            l[j].next = l[n]
            l[n].next = l[j+1]
            j+=1
            n-=1
        l[n].next = None
    elif n%2 == 1:
        j=0
        while n > j+1:
            l[j].next = l[n]
            l[n].next = l[j+1]
            j+=1
            n-=1
        l[j].next = l[n]
        l[n].next = None
        
