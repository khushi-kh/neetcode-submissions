class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)

        i = 0
        while i < len(nums):

            temp = 1
            
            for j in range(len(nums)):
                if j != i:
                    temp *= nums[j]

            output[i] = temp
            i += 1

        return output
