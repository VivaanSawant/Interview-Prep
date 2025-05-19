class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        
        j = 0
        while j < len(s):
            i = j + 1
            while i <= len(s):
                if s[j:i] in wordSet:
                    break
                i += 1
            if i > len(s):
                return False
            j = i
        return True
