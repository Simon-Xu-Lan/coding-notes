# Defination of Treenode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# To find all nodes in a binary tree
def findNodes(node, nodes):
    """
    @param self:
    @param node: the root node
    @param nodes: A list to put all nodes find from node
    @return: None
    """
    if not node:
        return
    nodes.append(node)
    findNodes(node.left, nodes)
    findNodes(node.right, nodes)

# To find all path in a binary tree from root node to leaf nodes
# 给一棵二叉树，找出从根节点到叶子节点的所有路径。
def findPaths(node, path, paths):
    """
    @param node: current node
    @param path: all nodes in the path from root to current node
    @param paths: a list to put all paths, the path is from root node to leaf node, 用于存储找到的所有点
    @return: None
    """

    if not node:
        return

    # Leaf node
    if not node.left and not node.right:
        paths.append("->".join([str(node.val) for node in path]))
        return

    path.append(node.left)
    findPaths(node.left, path, paths)
    path.pop() # This is backtracking for variable path

    path.append(node.right)
    findPaths(node.right, path, paths)
    path.pop() # This is backtracking for variable path