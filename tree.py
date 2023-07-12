# 层序便利
# 奇数从左向右，偶数从右向左

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
    # 标识位，判断当前层是否是奇数层，一开始表示的是第0层，所以值是False
    is_odd_level = False

    while queue:
        # level_size：当前层的节点个数
        level_size = len(queue)
        # current_level：存储当前层节点值的列表
        current_level = []
        # 遍历当前层的节点
        for i in range(level_size):
            node = queue.pop(0)
            # 奇数层从左向右
            if is_odd_level:
                current_level.append(node.val)
            # 偶数层从右向左
            else:
                current_level.insert(0, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # 遍历完一层加到结果中
        result.append(current_level)
        # 切换到下一层时，反转
        is_odd_level = not is_odd_level
    return result

# 创建一个二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# 进行层次遍历
result = levelOrder(root)
print(result)