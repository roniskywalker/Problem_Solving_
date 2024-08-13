class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        @cache
        def dp(i: int, j: int) -> bool:
            if i < 0 and j < 0: return True
            ans = False
            if i >= 0 and s1[i] == s3[i + j + 1]: ans |= dp(i - 1, j)
            if j >= 0 and s2[j] == s3[i + j + 1]: ans |= dp(i, j - 1)
            return ans
        return dp(m - 1, n - 1)