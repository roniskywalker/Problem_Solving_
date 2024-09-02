class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s+=1
                e-=1
        l, k = len(nums), k % len(nums)
        s, e = 0, l-1
        reverse(s, e)
        s, e = 0, k-1
        reverse(s, e)
        s, e = k, l-1
        reverse(s, e)