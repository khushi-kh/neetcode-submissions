class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp = {}

        for i in range(len(nums)):

            j = target - nums[i]

            if j in temp:
                return [temp[j], i]
            else:
                temp[nums[i]] = i
        