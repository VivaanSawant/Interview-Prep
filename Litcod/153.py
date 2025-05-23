class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binsearch(nums, lo, hi):
            if lo >= hi:
                return nums[lo]
            if hi - lo == 1:
                return min(nums[hi], nums[lo])

            mid = lo + ((hi - lo) // 2)
            loMid = lo + (mid - lo) // 2
            hiMid = mid + (hi - mid) // 2
           
            if nums[mid] > nums[hi]:
                return binsearch(nums, mid + 1, hi)
            else:
                return binsearch(nums, lo, mid)

        return binsearch(nums, 0, len(nums) - 1)
