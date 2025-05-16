class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = 0
        finalCount = 0

        numSet = set()
        for x in nums:
            numSet.add(x)
        
        for x in numSet:
            if (x-1) not in numSet:
                counter = 1
                while((x + 1) in numSet):
                    x += 1
                    counter += 1
            if counter > finalCount:
                finalCount = counter
        
        return finalCount
