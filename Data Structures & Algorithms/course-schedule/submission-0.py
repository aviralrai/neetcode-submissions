class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0] * numCourses
        for v,u in prerequisites:
            adj[u].append(v)
            indeg[v] += 1
        q = deque(i for i in range(len(indeg)) if indeg[i] == 0)
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return len(order) == numCourses

        