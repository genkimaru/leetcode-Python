
``` python
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
```

解释如下:

1. 定义函数`knapsack(w, wt, val, n)`接受4个输入参数:
   - `w`: 背包容量
   - `wt`: 每个物品的重量列表
   - `val`: 每个物品的价值列表
   - `n`: 物品数量
2. 创建一个二维数组`dp`来存储中间计算结果。其中`dp[i][j]`表示前`i`个物品放入容量为`j`的背包可以获得的最大价值。
3. 使用双重循环填充`dp`数组。对于每个物品`i`和背包容量`j`:
   - 如果当前物品重量`wt[i-1]`小于等于当前容量`j`，则有两种选择:
     1. 不放该物品,最大价值为`dp[i-1][j]`
     2. 放该物品,最大价值为`dp[i-1][j-wt[i-1]] + val[i-1]`
     取两者中较大的值作为`dp[i][j]`的值。
   - 如果当前物品重量大于当前容量,则`dp[i][j] = dp[i-1][j]`,沿用上一个状态的最大价值。
4. 最终返回`dp[n][w]`,即为最优解。

该算法的时间复杂度为O(n*W),空间复杂度为O(n*W),其中n为物品数量,W为背包容量。