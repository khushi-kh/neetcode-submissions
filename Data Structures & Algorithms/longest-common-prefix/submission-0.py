class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""

        isTrue = True

        i = 0

        while isTrue:

            for j in range(len(strs)):
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
        