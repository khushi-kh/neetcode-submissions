class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        arr = [[] for _ in range(len(nums))]

        for num, cnt in freq.items():
            arr[cnt-1].append(num)

        result = []

        for i in range(len(arr)-1, -1, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result