from collections import deque
from typing import List
class Solution:
    # 使用 拓扑排序 验证一个图是否是 DAG
    _prev_indegree = []
    def canFinish( self , courseNums: int, arr: List[List[int]]) -> bool:
        ## 设置入度数组
        indegree = [ 0  for _ in range(courseNums)] 

        if arr:
            for pair in arr:
                indegree[pair[0]] = indegree[pair[0]] + 1
        else:
            return True
        
        result = self.is_zero(indegree)

        if result:
            return True
        else:
            if self.is_not_changed(indegree):
                return False
            else:
                new_arr = []
                for pair in arr:
                    if indegree[pair[1]] != 0:
                        new_arr.append(pair)
                self._prev_indegree = indegree
                return self.canFinish(courseNums , new_arr)

    def is_zero(self , indegree):
        return len(list(filter(lambda x : x == 0  , indegree))) == len(indegree)
    
    def is_not_changed(self , indegree):
        if self._prev_indegree:
            return indegree == self._prev_indegree
        else:
            return False

# 示例
## [a , b] ,可以表示为 b -> a
# print(canFinish(2, [[1, 0]]))  # 返回 True
# print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # 返回 False
# r = canFinish(6 , [[0,1],[0,2],[1,2],[2,0],[0,4],[3,5]])

# print(Solution().canFinish(20 , [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))