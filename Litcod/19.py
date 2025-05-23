# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        if (head.next == None) and n == 1:
            return None
        

        j = head
        curr = j
        for i in range(0, n):
            curr = curr.next
        
        while curr.next != None:
            j = j.next
            curr = curr.next
        
        j.next = j.next.next

        return head
        