class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maximum = minimum = result = nums[0]

        for i in range(1, len(nums)):
            maximum = max(nums[i], nums[i] * maximum, nums[i] * minimum)
            minimum = min(nums[i], nums[i] * maximum, nums[i] * minimum)
            result = max(result, maximum) 


        return result


