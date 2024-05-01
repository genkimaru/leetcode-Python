from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0

        for i in range(n):
            ## 能不能到达重点的本质是 max_reach 和 i 的比较。
            if i  > max_reach: 
                return False
            max_reach = max(max_reach, i + nums[i])

        return True


nums = [3,2,1,0,1]
print(Solution().canJump(nums))