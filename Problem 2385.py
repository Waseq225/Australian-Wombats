# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root, start):
        # Improved DFS to build graph
        def dfs(node, parent):
            if node:
                if parent is not None:
                    graph[node.val].append(parent.val)
                if node.left:
                    graph[node.val].append(node.left.val)
                    dfs(node.left, node)
                if node.right:
                    graph[node.val].append(node.right.val)
                    dfs(node.right, node)

        graph = defaultdict(list)
        dfs(root, None)  # Building the graph with a single DFS pass
        visited = set()
        queue = deque([start])
        time = -1

        # BFS to find the maximum time to infect all nodes
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time

