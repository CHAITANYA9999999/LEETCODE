class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.mid(head)
        temp = right.next
        right.next = None
        right = temp

        leftSide = self.sortList(left)
        rightSide = self.sortList(right)
        return self.merge(leftSide, rightSide)

    def mid(self, head):
        print(head.val)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1,list2):
        dummy = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next