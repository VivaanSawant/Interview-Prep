class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solSet = set()  # Use a set to avoid duplicate triplets

        for i in range(len(nums)):
            target = -nums[i]
            seen = set()
            newArr = nums[:i] + nums[i + 1:]

            for x in newArr:
                complement = target - x
                if complement in seen:
                    triplet = tuple(sorted((nums[i], x, complement)))
                    solSet.add(triplet)
                seen.add(x)

        return [list(t) for t in solSet]

        