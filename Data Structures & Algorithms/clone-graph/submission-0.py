"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = {}
        q  = deque([node])
        d[node] = Node(node.val)
        while q:
            n1 = q.popleft()
            for neigh in n1.neighbors:
                if neigh not in d:
                    d[neigh] = Node(neigh.val)
                    q.append(neigh)
                d[n1].neighbors.append(d[neigh])
        return d[node]
                    
                    


        