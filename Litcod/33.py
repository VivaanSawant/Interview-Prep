class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binsearch(nums, lo, hi):
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            if lo >= hi:
                return -1

            mid = lo + ((hi - lo) // 2)

            if nums[mid] == target:
                return mid
            
            if target < nums[lo]:
                return binsearch(nums, mid + 1, hi)
            else:
                return binsearch(nums, lo, mid)

        return binsearch(nums, 0, len(nums) - 1)