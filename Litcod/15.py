class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solSet = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates for the first number
            
            target = -nums[i]
            k = i + 1
            j = n - 1

            while k < j:
                two_sum = nums[k] + nums[j]
                if two_sum < target:
                    k += 1
                elif two_sum > target:
                    j -= 1
                else:
                    solSet.append([nums[i], nums[k], nums[j]])
                    # Skip duplicates for nums[k] and nums[j]
                    while k < j and nums[k] == nums[k + 1]:
                        k += 1
                    while k < j and nums[j] == nums[j - 1]:
                        j -= 1
                    k += 1
                    j -= 1

        return solSet
