class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        sublist = [False for _ in range(0, len(s) + 1)]

        wordSet = set(wordDict)

        i = j = 0

        sublist[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordSet and sublist[j]:
                    sublist[i] = True
                    break
        
        return sublist[len(s)]




        