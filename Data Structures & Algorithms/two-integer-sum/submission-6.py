class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = {}

        for i in range(len(nums)):

            num = nums[i]

            if target-num in result:
                return [result[target-num], i]
            else:
                result[num] = i