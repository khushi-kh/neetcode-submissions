class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1: return strs[0]

        if len(strs) == 0: return ""

        strs = sorted(strs)

        result = ""

        for i in range(len(strs[0])):

            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                return result

        return result