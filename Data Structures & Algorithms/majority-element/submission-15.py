import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 1 or len(nums) == 2: return nums[0]

        freq = {}
        n = len(nums)

        for num in nums:
            if num in freq:
                freq[num] += 1
                if freq[num] > n//2:
                    return num
            else:
                freq[num] = 1

