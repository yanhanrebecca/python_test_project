class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    # 如果根节点为空，则返回空列表
    if not root:
        return []

    result = []
    # 使用队列来进行层次遍历，将根节点入队列
    queue = [root]

    while queue:
        # level_size：当前层的节点个数
        level_size = len(queue)
        # current_level：存储当前层节点值的列表
        current_level = []
        # 遍历当前层的节点
        for i in range(level_size):
            # 弹出队列中的第一个节点，并且将将节点值添加到当前层列表current_level中
            node = queue.pop(0)
            current_level.append(node.val)
            # 层次遍历是从左到右的，先判断是否有左孩子
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 遍历完一层加到结果中
        result.append(current_level)

    return result

# 创建一个二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
# 进行层次遍历
result = levelOrder(root)
print(result)  # 输出 [[1], [2, 3], [4, 5]]