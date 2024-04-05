class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0
            while n:
                output += (n%10)**2
                n = n // 10
            return output 
        map = set()
        while n:
            if n in map:
                return False
            map.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True