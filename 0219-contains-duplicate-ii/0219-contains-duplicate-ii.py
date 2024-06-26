class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i
            else:
                if abs(i - map[nums[i]]) <= k:
                    return True
                map[nums[i]] = i
        return False