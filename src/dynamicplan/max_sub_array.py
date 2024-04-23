# 连续最大和的数组子串，かだね算法实现：
#　动态规划问题，需要维护两个变量，当前最优解和全局最优解。
#  通过比较当前元素和当前元素与之前所有元素的和的比较，得到当前最优解。
#  通过比较当前最优和全局最优解的比较，更新全局最优解。
#  返回全局最优解。
class MaxSubArray:
    def max_subarray_sum(self , arr):
        max_sum = float('-inf')
        current_sum = 0
        for ele in arr:
            current_sum = max(ele , current_sum + ele)
            max_sum = max(current_sum , max_sum)
        return max_sum

arr = [1,-1,-2,-3,3,4]
max_sum = MaxSubArray().max_subarray_sum(arr)
print(max_sum)





