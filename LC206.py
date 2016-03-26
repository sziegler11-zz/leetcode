class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None




def reverseList(head):
        if head==None or head.next == None:
            return head
        prev2 = head
        head = head.next
        while head != None:
            prev1 = head
            head = head.next
            prev1.next = prev2
            prev2=prev1
            print 'prev2 val= ' + str(prev2.val)+'\n'
            print 'prev1 val= ' + str(prev1.val)+'\n'
            if head!=None:
                print 'head val= ' + str(head.val)+'\n'
            print '------- \n'
        return prev1
