#This code appears to work, but it's too slow for leetcode

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(head):
        newHead = head
        if head == None or head.next==None:
            return head
        curr= head.next

        while curr != None:
            u=newHead
            v=None
            while curr.val > u.val:
                v=u
                u=u.next
            if u == newHead:
                newHead = curr
            if u == curr:
                curr=curr.next
            else:
                temp = curr.next
                curr.next = u
                if v != None:
                    v.next = curr
                while u.next != curr:
                    u=u.next
                u.next = temp
                curr = temp
        return newHead

t=ListNode(3)
t.next=ListNode(4)
t.next.next=ListNode(1)
t.next.next.next=ListNode(9)
t.next.next.next.next=ListNode(8)

s=insertionSortList(t)
