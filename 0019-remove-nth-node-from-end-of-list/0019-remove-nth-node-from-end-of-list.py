class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
        
        prev = dummy
        cur = head
        next = cur.next
        for i in range(length-n):
            prev = cur
            cur = next
            next = next.next
        
        if not next:
            prev.next = None
            return dummy.next
        
        prev.next = next
        return dummy.next