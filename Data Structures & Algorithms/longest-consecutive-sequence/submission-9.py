class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        temp = set(nums)
        temp = list(temp)
        temp.sort()

        curr = 1
        streak = 1

        for i in range(len(temp)-1):
            
            if temp[i] == temp[i+1] - 1:
                curr += 1
            
            else:
                curr = 1

            streak = max(curr, streak)
            

        return streak
            