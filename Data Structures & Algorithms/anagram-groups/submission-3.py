class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for string in strs:
            
            key = [0] * 26

            for s in string:
                temp = ord(s) - ord('a')
                key[temp] += 1

            result[tuple(key)].append(string)


        return list(result.values())