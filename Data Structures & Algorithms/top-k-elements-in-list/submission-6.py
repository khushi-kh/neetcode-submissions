class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        hp = []

        for num in freq.keys():
            heapq.heappush(hp,(freq[num], num))
            
            if len(hp) > k:
                heapq.heappop(hp)

        result = []
        for i in range(k):
            result.append(heapq.heappop(hp)[1])

        return result