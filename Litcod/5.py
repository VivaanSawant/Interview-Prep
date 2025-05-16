import heapq
class Solution(object):
    def __checkPalindrome(self, str):
        front = 0
        back = len(str) - 1
        while(front != back and front < back):
            if(str[front] != str[back]):
                return False
            front += 1
            back -= 1
        return True
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromes = []
        for i in range(0, len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                substr = s[i:j + 1]
                length = len(substr)
                if(self.__checkPalindrome(substr)):
                        palindromes.append((-length, substr))
                        if(len(substr) == len(s)):
                            return substr
        heapq.heapify(palindromes)
        maxTup = heapq.heappop(palindromes)
        return maxTup[1]


    