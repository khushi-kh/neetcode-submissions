class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums
        # return ans

        n = len(nums)

        ans = [0] * (n * 2)

        # for i in range(n):
        #     ans[i], ans[i+n] = nums[i], nums[i]

        # return ans

        for i in range(2 * n):
            ans[i] = nums[i%n]
        return ans