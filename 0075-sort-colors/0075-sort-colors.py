class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0
        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1