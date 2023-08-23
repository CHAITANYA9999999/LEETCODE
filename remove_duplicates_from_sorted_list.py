# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head==None:
            return head
        dup=head
        temp=head.next
        
        while temp:
            if temp.val == dup.val:
                dup.next=temp.next
            else:
                dup=temp
            temp=temp.next
        return head