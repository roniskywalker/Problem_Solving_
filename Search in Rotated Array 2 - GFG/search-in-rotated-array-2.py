#User function Template for python3

class Solution:
    def Search(self, n, A, key):
        l, h = 0, n-1
        while l <= h:
            mid = l + (h - l) // 2
            if A[mid] == key:
                return 1
            elif A[l] == A[mid] and A[mid] == A[h]:
                l += 1
                h -= 1
                continue
            elif A[l]<=A[mid]:
                if A[l]<=key and key<=A[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if A[mid]<=key and key<=A[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends