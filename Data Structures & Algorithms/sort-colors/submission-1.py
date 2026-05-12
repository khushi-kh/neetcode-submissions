class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force
        zeroes = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            else: twos += 1

        for i in range(zeroes):
            nums[i] = 0

        for i in range(zeroes, zeroes + ones):
            nums[i] = 1
        
        for i in range(zeroes + ones, len(nums)):
            nums[i] = 2


        