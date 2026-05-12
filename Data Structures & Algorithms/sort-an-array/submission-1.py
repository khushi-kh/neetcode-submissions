class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort

        n = len(nums)

        for i in range(n):
            flag = 0

            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag += 1

            if flag == 0:
                return nums

        return nums