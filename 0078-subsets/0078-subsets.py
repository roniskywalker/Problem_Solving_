class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def create(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            create(i + 1)
            subset.pop()
            create(i + 1)
        create(0)
        return res