from typing  import List

## 利用单调Stack 
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            top_index = stack.pop()
            area = heights[top_index] * (index - stack[-1] - 1 if stack else index)
            print(heights[top_index] , (index - stack[-1] - 1 if stack else index))
            max_area = max(max_area, area)

    
    while stack:
        top_index = stack.pop()
        area = heights[top_index] * (index - stack[-1] - 1 if stack else index)
        print(heights[top_index] , (index - stack[-1] - 1 if stack else index))
        max_area = max(max_area, area)

    return max_area



heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))

#[]                                 
#[0]
#[]
#[1]
#[1, 2]
#[1, 2, 3]
#[1, 2]
#[1]
#[1, 4]
#[1, 4, 5]
#[1, 4]
#[1]
#10
        

#0
#0
#2
#2
#2
#2
#6
#10
#10
#10
#10
#10
#10


#2 1
#6 1
#5 2
#3 1
#2 4
#1 6
#10