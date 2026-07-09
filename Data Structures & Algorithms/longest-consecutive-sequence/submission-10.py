class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        temp = set(nums)
        streak = 0

        for num in temp:

            if num-1 not in temp:
                curr = 1

                while (num + curr) in temp:
                    curr += 1
                
                streak = max(curr, streak)

        return streak
                