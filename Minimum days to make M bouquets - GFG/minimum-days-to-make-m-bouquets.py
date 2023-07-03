#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isPossible(self, bloomDay, m, k, day):
        cnt, no_of_bouquets = 0, 0
        
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                cnt += 1
            else:
                no_of_bouquets += cnt // k
                cnt = 0
        no_of_bouquets += cnt // k
        if no_of_bouquets >= m:
            return True
        return False
        
    def solve(self, m, k, bloomDay):
        if (m*k > len(bloomDay)): return -1
        
        low, high = min(bloomDay), max(bloomDay)
        
        while(low <= high):
            mid = low + (high - low) // 2
            
            if self.isPossible(bloomDay, m, k, mid):
                high = mid - 1
            else:
                low = mid + 1
                
        return low
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        M, K = list(map(int, input().split()))
        bloomDay = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(M, K, bloomDay)
        print(res)
# } Driver Code Ends