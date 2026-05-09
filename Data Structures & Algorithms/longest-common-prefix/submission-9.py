class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = min(strs, key=len)

        for i in range(len(result)):

            for j in range(1, len(strs)):
                if result[i] != strs[j][i]:
                    return result[:i]

        return result