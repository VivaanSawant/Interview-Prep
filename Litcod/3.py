class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # look thru all substrings, put seen letters in a hash set, end substring once letters found
        finalCount = 0
        for i in range(0, len(s)):
            substring = s[i:]
            count = 0
            letters = set()
            for x in substring:
                if x in letters:
                    break
                else:
                    letters.add(x)
                    count += 1
            if count > finalCount:
                finalCount = count
        return finalCount