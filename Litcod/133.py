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
        oldNew = {}
        queue = [node]
        oldNew[node] = Node(node.val)
        
        while(len(queue) > 0):
            curr = queue.pop()
            if curr not in oldNew:
                oldNew[curr] = Node(curr.val)

            for x in curr.neighbors:
                if x not in oldNew:
                    queue.append(x)
                if x in oldNew:
                    oldNew[curr].neighbors.append(oldNew[x])
        
        return oldNew[node]

            

        

                
            
