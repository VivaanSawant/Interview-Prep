# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodeArr = []
        curr = head
        while(curr != None):
            nodeArr.append(curr)
            curr = curr.next

        n = len(nodeArr)
        for i in range(1, n, 2):
            lastNode = nodeArr.pop()
            nodeArr.insert(i, lastNode)
            

        #reconstruct LL
        for i in range(0, len(nodeArr) - 1):
            nodeArr[i].next = nodeArr[i + 1]
        nodeArr[len(nodeArr) - 1].next = None

