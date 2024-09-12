class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1
        for i in nums:
            if i == 0:
                cur_max = cur_min = 1
            else:
                temp_max = i * cur_max
                temp_min = i * cur_min
                cur_max = max(temp_max, temp_min, i)
                cur_min = min(temp_max, temp_min, i)
                res = max(res, cur_max)
        return res