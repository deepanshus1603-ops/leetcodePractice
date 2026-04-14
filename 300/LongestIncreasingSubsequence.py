class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[-1]=1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
                else:
                    dp[i]=max(dp[i],1)
        return max(dp)
