class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freq_s = {}
        freq_t = {}

        # for char in s:
        #     if char in freq_s:
        #         freq_s[char] += 1
        #     else:
        #         freq_s[char] = 1

        # for char in t:
        #     if char in freq_t:
        #         freq_t[char] += 1
        #     else:
        #         freq_t[char] = 1

        # single loop
        for i in range(len(s)):
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)

        return freq_s == freq_t