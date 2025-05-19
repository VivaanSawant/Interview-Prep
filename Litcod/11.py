import heapq
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def findHeight(i, j):
            return min(height[i], height[j]) * (j - i)
        
        allHeights = []
        for i in range(0, len(height)):
            for j in range(i, len(height)):
                allHeights.append(-findHeight(i, j))
        heapq.heapify(allHeights)
        return -heapq.heappop(allHeights)

        

        

        