class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion sort

        n = len(nums)

        for i in range(1,n):

            j = i - 1
            current = nums[i]

            while j >= 0 and current < nums[j]:

                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = current

        return nums
                