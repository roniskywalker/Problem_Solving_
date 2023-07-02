#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
        low, high, ans = 1, x//2, 1
        
        while(low<=high):
            mid = low + (high-low) // 2
            
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends