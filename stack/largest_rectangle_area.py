from typing  import List

## 暴力法
def largest_rectangle_area(heights : List[int]) -> int:
    if not heights:
        return 0
    
    max_area = 0
    for i in range(len(heights)):
        right_i = i 
        left_i = i
        while right_i < len(heights) - 1 and heights[right_i + 1]  >= heights[i] :
            right_i += 1
        while left_i > 0 and heights[left_i - 1 ] >= heights[i]:
            left_i -= 1
        max_area = max(max_area , ( right_i - left_i + 1 ) * heights[i])
    
    return max_area

heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))
        

