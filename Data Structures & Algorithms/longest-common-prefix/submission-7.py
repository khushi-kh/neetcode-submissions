class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        result = ""

        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return result
            else:
                result += strs[0][i]

        return result