class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1

        temp = set(nums)
        
        res = 0

        for num in nums:
            streak = 0
            curr = num

            while curr in temp:
                streak += 1
                curr += 1

            res = max(streak, res)

        return res