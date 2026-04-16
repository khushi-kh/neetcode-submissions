class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freq_s = {}
        freq_t = {}

        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1

        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1


        for key in freq_s:
            try:
                if freq_s[key] != freq_t[key]:
                    return False
            except KeyError:
                return False
        return True