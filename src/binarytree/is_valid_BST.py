class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return isValidBST(root.left, min_val, root.val) and isValidBST(root.right, root.val, max_val)

# 测试
# 构建一个合格的二叉树
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValidBST(root))  # 输出 True

# 构建一个不合格的二叉树
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(isValidBST(root))  # 输出 False