class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1

        temp = set(nums)
        temp = list(temp)
        temp.sort()

        result = []
        ans = 0

        for i in range(len(temp)-1):
            
            if temp[i] == temp[i+1] - 1:
                result.append(temp[i])

                if i == len(temp) - 2:
                    result.append(temp[i])
            
            else:
                result.append(temp[i])

                if len(result) > ans:
                    ans = len(result)
                    
                result = []

            if len(result) > ans:
                ans = len(result)
            

        return ans
            