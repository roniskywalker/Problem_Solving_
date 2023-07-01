#User function Template for python3

import sys

class Solution:
    def findKRotation(self,arr,  n):
        l, h, ans, index = 0, n-1, sys.maxsize, -1
        
        while(l <= h):
            mid = l + (h-l) // 2
            
            if arr[l] <= arr[h]:
                if ans > arr[l]:
                    ans = arr[l]
                    index = l
                break
                
            elif arr[l] <= arr[mid]:
                if ans > arr[l]:
                    ans = arr[l]
                    index = l
                l = mid + 1
                
            else:
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = mid
                h = mid - 1
                
        return index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends