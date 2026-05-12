class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        result = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < (min(len(strs[i]), len(result))):
                if strs[i][j] != result[j]:
                    break
                j += 1
            result = result[:j]

        return result
        