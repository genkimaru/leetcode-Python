def min_window(s, t):
    target_map = {}
    for char in t:
        if char in target_map:
            target_map[char] += 1
        else:
            target_map[char] = 1
    
    left = 0
    right = 0
    min_len = float('inf')
    min_start = 0
    target_count = len(t)
    
    while right < len(s):
        if s[right] in target_map:
            if target_map[s[right]] > 0:
                target_count -= 1
            target_map[s[right]] -= 1
        
        right += 1
        
        while target_count == 0:
            if right - left < min_len:
                min_len = right - left
                min_start = left
            
            if s[left] in target_map:
                target_map[s[left]] += 1
                if target_map[s[left]] > 0:
                    target_count += 1
            
            left += 1
    
    if min_len == float('inf'):
        return ""
    
    return s[min_start:min_start+min_len]

# 测试
s = "a"
t = "aa"
print(min_window(s, t))  # 输出"BANC"