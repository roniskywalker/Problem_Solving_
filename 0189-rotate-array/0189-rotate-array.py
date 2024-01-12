class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l, k = len(nums), k % len(nums)
        s, e = 0, l-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        s, e = 0, k-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        s, e = k, l-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1