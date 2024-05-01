class Solution:
    def canJump(self , nums):
        max_reach = 0
        for i in nums:
            if i > max_reach:
                return False
            max_reach = max(max_reach , nums[i] + i)
        return True



nums = [3,2,1,0,1]
print(Solution().canJump(nums))