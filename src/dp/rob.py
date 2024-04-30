from typing import List

"""
打家劫舍。
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] 
        if len(nums) >= 2:

            ## 初始化dp 以及第一个和第二个结果。
            dp  = [0] * (len(nums) + 1 )
            dp[1] = nums[0]
            dp[2] = max(nums[0] , nums[1])
        
            ## 从3 开始
            for i in range(3 , len(nums) + 1):
                if i <= len(nums):
                    ## 接受第i个数字 dp[i -2] + nums[i -1] ，
                    #   或者是不接受  dp[i -1]
                    dp[i] = max(dp[i -2] + nums[i -1] , dp[i -1])
            
            print(dp)
            return dp[len(nums)]



nums = [1,2,3,1 ,8,1,1]
Solution().rob(nums)