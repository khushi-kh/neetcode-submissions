class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
                if freq[num] > len(nums)// 2:
                    return num
            else:
                freq[num] = 1

        