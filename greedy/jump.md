```python
def canJump(nums):
    n = len(nums)
    max_reach = 0

    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True
```

1. 首先获取输入数组 `nums` 的长度 `n`。
2. 初始化 `max_reach` 变量,用于记录当前可以到达的最远位置。
3. 遍历数组 `nums`,对于每个位置 `i`:
   - 如果 `i` 大于当前的 `max_reach`,说明无法到达该位置,返回 `False`。
   - 更新 `max_reach` 为当前 `max_reach` 和 `i + nums[i]` 的最大值。
4. 如果能遍历完整个数组,说明可以到达最后一个位置,返回 `True`。

这个解决方案的时间复杂度为 O(n),空间复杂度为 O(1),因为我们只使用了一个额外的变量 `max_reach`。

你可以将这个函数用在你的代码中,测试一下它的正确性。如果你有任何其他问题,欢迎随时询问我。