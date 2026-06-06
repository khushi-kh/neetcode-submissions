class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeroes = nums.count(0)

        if zeroes > 1:
            return [0] * len(nums)

        total = 1
        for num in nums:
            if num != 0:
                total *= num

        result = [0] * len(nums)

        if zeroes == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = total
            return result
            
        for i in range(len(nums)):
            result[i] = total // nums[i]
        return result

