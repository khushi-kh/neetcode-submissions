class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        for i in range(len(min(strs[0], strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return min(strs[0],strs[-1], key=len)[:i]

        return strs[0]