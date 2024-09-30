class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0], dp[1] = False, False
        for num in range(2,n):
            if dp[num]:
                for index in range(num*2, n, num):
                    dp[index] = False
        return sum(dp)