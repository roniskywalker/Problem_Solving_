class Solution:
    
    #Function to find minimum number of pages.
    def isPossible(self, A, page):
        n, student, no_of_pages = len(A), 1, 0
        
        for i in range(n):
            if A[i]+ no_of_pages <= page:
                no_of_pages += A[i]
            else:
                student += 1
                no_of_pages = A[i]
                
        return student
    
    def findPages(self,A, N, M):
        if M > N: return -1
        
        low, high = max(A), sum(A)
        
        while(low <= high):
            mid = low + (high - low) // 2
                
            if self.isPossible(A, mid) > M:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends