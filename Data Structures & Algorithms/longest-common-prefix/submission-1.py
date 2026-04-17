class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""

        smallest = min(strs)

        i = 0

        while i < len(smallest):

            for j in range(len(strs)):
                try:
                    if smallest[i] == strs[j][i]: continue
                    else:
                        return result
                except IndexError:
                    return result

            result += smallest[i]
            i += 1
        return result
        