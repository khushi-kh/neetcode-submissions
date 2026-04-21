class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for i in range(k):
            highest_freq = max(freq, key=freq.get)
            result.append(highest_freq)
            del freq[highest_freq]

        return result

        