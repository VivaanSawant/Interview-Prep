class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binsearch(nums, lo, hi):
            if lo > hi:
                return -1
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi

            mid = lo + ((hi - lo) // 2)

            if nums[mid] == target:
                return mid

         
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    return binsearch(nums, lo, mid - 1)
                else:
                    return binsearch(nums, mid + 1, hi)
            else:
                if nums[mid] < target <= nums[hi]:
                    return binsearch(nums, mid + 1, hi)
                else:
                    return binsearch(nums, lo, mid - 1)

        return binsearch(nums, 0, len(nums) - 1)
