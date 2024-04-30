
"""
总体来说，动态规划 dynamic programming 是 利用到 递归，通过解决小问题不断累计，从而解决大问题

"""

def knapsack(w , wt , val , n):
    ## 初始化 dp数组。 dp[i][j] 表示的意思是在 容量为j的时候，选择前i个物品可以得到的最大价值
    ## 注意，
    dp = [  [ 0 for j in range(w + 1)] for i in range(n +1)]

    for i in range(1 , n + 1):
        for j in range(1 , w + 1):
            if wt[i -1 ] <= j: ## 如果 第i个物品的重量小于 j
                ## 可以有两种选择， 
                # dp[i - 1][j] 不选 物品i ，则最大价值就是 只选i - 1 之前的物品的最大价值。
                # dp[i - 1][j - wt[i -1]] + val[i - 1]
                # 则价值为 没有选物品i的扣去物品i重量的最大价值 加上 物品i的价值。
                # 注意！！ wt[i - 1] 表示的是 物品i的重量。
                # 注意!!  val[i - 1]表示对而是 物品i的价值。
                #  因为数组 wt 和  val 都是从下标0 算起的，而 dp数组是从 1 算起的 ， 所以这地方的理解尤为关键。
                dp[i][j] = max(dp[i-1][j] , dp[i - 1][ j - wt[i -1]] + val[i - 1])
            else:
                dp[i][j] = dp[i -1][j]
    
    return dp[n][w]

# 示例使用
w = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = 3
print(knapsack(w, wt, val, n))  # 输出: 220
