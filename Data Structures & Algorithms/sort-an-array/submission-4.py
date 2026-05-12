class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort

        n = len(nums)

        for i in range(n):

            k = i

            for j in range(i, n):
                if nums[j] < nums[k]:
                    k = j

            nums[i], nums[k] = nums[k], nums[i]

        return nums