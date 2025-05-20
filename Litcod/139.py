class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set()
        for x in wordDict:
            wordSet.add(x)
        
        sublist = [False for _ in range(0, len(s) + 1)]

        sublist[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if sublist[j] and s[j:i] in wordSet:
                    sublist[i] = True
                    break
        
        return sublist[len(s)]
        