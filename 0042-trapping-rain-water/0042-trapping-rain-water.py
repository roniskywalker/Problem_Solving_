class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        quantity = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                quantity += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                quantity += right_max - height[r]
        return quantity