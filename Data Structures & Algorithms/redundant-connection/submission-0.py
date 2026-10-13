class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(a):
            root = a
            while parent[root] != root:
                root = parent[root]
            while parent[a] != root:
                parent[a], a = root, parent[a]
            return root
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
            return True
        V = 0
        for u,v in edges:
            V = max(V,u)
            V = max(V,v)
        parent = list(range(0,V+1))
        for u,v in edges:
            if not union(u,v):
                return [u,v]
             