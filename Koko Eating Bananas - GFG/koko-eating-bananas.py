#User function Template for python3
import math

class Solution:
    def totalHour(self, arr, hourly):
        n, total_hrs = len(arr), 0
        
        for i in range(n):
            total_hrs += math.ceil(arr[i]/hourly)
            
        return total_hrs
        
    def Solve(self, N, piles, H):
        low, high = 1, max(piles)
        
        while(low<=high):
            mid = low + (high - low) // 2
            total_hrs = self.totalHour(piles, mid)
            
            if (total_hrs <= H):
                high = mid - 1
            else:
                low = mid + 1
            
        return low

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends