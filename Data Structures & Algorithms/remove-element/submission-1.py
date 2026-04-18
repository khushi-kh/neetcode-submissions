class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = -1

        for j in range(len(nums)):
            if nums[j] == val:
                i = j
                break

        if i == -1: return len(nums)

        for j in range(i+1, len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        return i