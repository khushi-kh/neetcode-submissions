class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start, middle = 0, 0
        end = len(nums)-1

        while end >= middle:
            if nums[middle]== 0:
                nums[start], nums[middle] = nums[middle], nums[start]
                middle += 1
                start += 1

            elif nums[middle] == 1:
                middle += 1

            else:
                nums[end], nums[middle] = nums[middle], nums[end]        
                end -= 1