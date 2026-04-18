class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
       nums.sort()

       idx = len(nums)// 2
       return nums[idx]