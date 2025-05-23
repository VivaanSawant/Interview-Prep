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
            loMid = (mid - lo) // 2
            hiMid = mid + loMid
            print((lo, hi, loMid, mid, hiMid))
            if nums[hiMid] < nums[mid]:
                return binsearch(nums, mid, hi)
            elif nums[loMid] > nums[mid]:
                return binsearch(nums, lo, mid)
            else:
                return binsearch(nums, lo, mid)

        
        return binsearch(nums, 0, len(nums) - 1)

        