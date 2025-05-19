import heapq
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def findHeight(i, j):
            return min(height[i], height[j]) * (j - i)
        
        i = 0
        j = len(height) - 1

        res = 0

        while(i < j):
            res = max(res, findHeight(i, j))
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return res
        

        

        

        

        