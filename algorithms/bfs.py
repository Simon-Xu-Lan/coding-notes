class Solution:
    """
    @param root: A Tree
    @return: level order a list of integer
    """
    # 用单队列实现
    def levelOrder(self, root):
        if not root:
            return []

        # Step 1: 把第一层的节点放到队列中
        queue = collections.deque([root])
        results = []

        # Step 2: While队列非空
        while queue:
            # 把当前层节点的value生成一个list， 并放入results
            results.append([node.val for node in queue])
            # Step 3: 根据当前层的节点，拓展出下一层节点，并放入队列中
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return results


    # 用双队列实现
    def levelOrder2(self, root):
        if not root:
            return []

        results = []
        queue = [root]
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue

        return results


    # 用 Dummy node 实现
    def levelOrder2(self, root):
        if not root:
            return []

        queue = collections.deque([root, None])
        results = []
        level = []
        while queue:
            node = queue.popleft()
            if node is None:
                results.append(level)
                level = []
                if queue:
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return results
