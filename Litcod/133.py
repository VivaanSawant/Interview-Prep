"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        oldNew = {}
        stack = [node]
        oldNew[node] = Node(node.val)
        
        while(len(stack) > 0):
            curr = stack.pop()
                
            for x in curr.neighbors:
                if x not in oldNew:
                    oldNew[x] = Node(x.val)
                    stack.append(x)
                if x in oldNew:
                    oldNew[curr].neighbors.append(oldNew[x])
        
        return oldNew[node]

            

        

                
            
