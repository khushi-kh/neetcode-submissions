class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        arr = []
        for num, cnt in freq.items():
            arr.append([num, cnt])

        arr.sort(key=lambda x:x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(arr[i][0])

        return result