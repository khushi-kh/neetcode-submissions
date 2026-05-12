class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for ch in s:
                temp = ord(ch) - ord('a')
                key[temp] += 1
            result[tuple(key)].append(s)

        return list(result.values())
            