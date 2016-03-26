class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def insertsort(head):
    heady = head
    l = {}
    l[head] = head.val
    while heady.next != None:
        v = heady.next
        for key in l:
            if heady.val < key.val:
                heady.next = key
                for yek in l:
                    if yek.next == key:
                        yek.next = heady
        heady = v
        
    for key in l:
        luey = True
        for yek in l:
            if yek.next == key:
                luey = False
        if luey == True:
            return key

    return None
    
        
t=ListNode(3)
t.next=ListNode(2)

insertsort(t)
