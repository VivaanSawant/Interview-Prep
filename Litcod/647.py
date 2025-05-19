class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        def countPalindrome(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        for i in range(0, len(s)):
            count += countPalindrome(i, i)
            count += countPalindrome(i, i + 1)
        return count