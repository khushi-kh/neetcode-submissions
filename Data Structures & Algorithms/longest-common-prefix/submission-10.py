class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_str = min(strs)
        max_str = max(strs)

        for i in range(len(min(min_str, max_str, key=len))):
            if min_str[i] != max_str[i]:
                return min_str[:i]

        return min_str