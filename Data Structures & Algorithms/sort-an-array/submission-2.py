class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort

        n = len(nums)

        for i in range(n):
            flag = False

            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True

            if flag == False:
                return nums

        return nums