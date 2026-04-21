class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []

        for i in range(k):
            max_cnt = 0
            cnt = 0
            max_cnt_element = -1
            for num in nums:
                if num not in result:
                    cnt = nums.count(num)
                    max_cnt = max(max_cnt, cnt)
                    if max_cnt == cnt:
                        max_cnt_element = num

            result.append(max_cnt_element)

        return result

        