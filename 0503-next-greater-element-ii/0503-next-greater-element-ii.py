class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = list(range(n))
        st = []
        for i in range(2*n-1, -1, -1):
            while len(st) != 0 and nums[i%n] >= st[-1]:
                st.pop()
            if i<n:
                nge[i] = st[-1] if len(st) != 0 else -1
            st.append(nums[i%n])
        return nge