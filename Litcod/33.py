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
            
            print(lo, mid, hi)
            
            if target < nums[lo]:
                return binsearch(nums, mid + 1, hi)
            elif target > nums[hi]:
                return binsearch(nums, lo, mid)
            else:
                if target < nums[mid]:
                    return binsearch(nums, lo, mid)
                else:
                    return binsearch(nums, mid + 1, hi)

        return binsearch(nums, 0, len(nums) - 1)