#User function Template for python3

class Solution:
    def isPossible(self, stalls, n, k, mid):
        cow_count, last = 1, stalls[0]
        
        for i in range(1,n):
            if stalls[i] - last >= mid:
                cow_count += 1
                last = stalls[i]
        
        if cow_count >= k:
            return True
        return False
        
    def solve(self,n,k,stalls):
        stalls.sort()
        low, high = 0, max(stalls) - min(stalls)
        
        while(low <= high):
            mid = low + (high - low) // 2
            
            if self.isPossible(stalls, n, k, mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends