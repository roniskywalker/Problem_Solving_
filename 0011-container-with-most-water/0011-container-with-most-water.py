class Solution:
    def maxArea(self, height: List[int]) -> int:
        final_area = 0
        l, r = 0, len(height)-1

        while l < r:
            area = (r-l)*(min(height[l], height[r]))
            final_area = max(area, final_area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                if l+1 < r-1 and height[l+1] > height[r-1]:
                    l += 1
                else:
                    r -= 1
        return final_area