class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        if len(strs) == 0: return ""

        result = ""

        smallest = min(strs)

        i = 0

        while i < len(smallest):

            for j in range(len(strs)):
                    if smallest[i] == strs[j][i]: continue
                    else:
                        return result

            result += smallest[i]
            i += 1
        return result
        