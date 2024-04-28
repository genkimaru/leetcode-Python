from typing  import List

## 利用单调Stack 
def largest_rectangle_area(heights):
    stack = []
    index = 0
    max_area = 0
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            stack_top_index = stack.pop()
            area = heights[stack_top_index] * ( index - stack[-1] -1  if stack else index)
            max_area = max(max_area , area)
    
    while stack:
            stack_top_index = stack.pop()
            area = heights[stack_top_index]
            max_area = max(max_area , area)
    
    return max_area










heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))