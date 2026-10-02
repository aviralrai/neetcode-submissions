class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = set()
        stack = []
        count = 0
        for node in range(n):
            if node in visited:
                continue
            visited.add(node)
            count += 1
            stack.append(node)
            while stack:
                n1 = stack.pop()
                for neigh in g[n1]:
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)
        return count
        