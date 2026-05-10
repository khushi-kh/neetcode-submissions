class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        answer = max_count = 0

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] > max_count:
                max_count = freq[num]
                answer = num

        return answer