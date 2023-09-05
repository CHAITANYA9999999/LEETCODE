"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        d={}
        temp=head
        while temp:
            d[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            d[temp].next=d.get(temp.next)
            d[temp].random=d.get(temp.random)
            temp=temp.next
        return d[head]