class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax,curmin=0,0
        maxi=nums[0]
        mini=nums[0]
        for i in nums:
            curmax=max(curmax+i,i)
            maxi=max(maxi,curmax)
            curmin=min(curmin+i,i)
            mini=min(mini,curmin)
        if maxi>0 :
            return max(maxi,sum(nums)-mini) 
        else:
            return maxi