from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    indegree = [0] * numCourses
    graph = defaultdict(list)
    
    for course, pre in prerequisites:
        indegree[course] += 1
        graph[pre].append(course)
    
    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        course = queue.popleft()
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return all(indegree[i] == 0 for i in range(numCourses))

# 示例
## [a , b] ,可以表示为 b -> a
print(canFinish(2, [[1, 0]]))  # 返回 True
print(canFinish(2, [[1, 0], [0, 1]]))  # 返回 False