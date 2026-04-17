class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        if len(strs) == 0: return ""

        result = ""

        isTrue = True

        i = 0

        while isTrue:

            for j in range(1,len(strs)):
                try:
                    if strs[0][i] == strs[j][i]: continue
                    else:
                        isTrue = False
                except IndexError:
                    return result

            if isTrue:
                    result += strs[0][i]
                    i += 1
        return result
        