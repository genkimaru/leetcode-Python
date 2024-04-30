from typing import List
"""
换钱。

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        ## 去掉大于amount的 coins
        coins = list(filter(lambda x : x <= amount , coins ))
        if not coins:
            return -1
        if amount < min(coins):
            return -1

        ## 初始化dp
        dp = [ 0 ] *( amount+ 1)

        for i in coins:
            dp[i] = 1

        dp[1:min(coins)] = [ float('inf') ] * (min(coins) - 1)

        for i in range(min(coins) , amount+1):
            min_count = float('inf')
            j = i 
            while j <= i and j >= min(coins):
                if j in coins :
                    min_count = min(min_count , 1 + dp[i - j])
                j -= 1
            dp[i] = min_count

        return dp[amount] if dp[amount] != float('inf') else -1 

coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))

