class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,d in times:
            g[u].append((v,d))
        INF = float('inf')
        dist = [INF] * (n+1)
        done = [False] * (n+1)
        dist[k] = 0
        pq = [(0,k)]

        while pq:
            d, u = heapq.heappop(pq)
            if done[u]: continue
            done[u] = True

            for v, wd in g[u]:
                nd = d + wd
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq,(nd, v))
        res = max(dist[1:])
        return -1 if res == INF else res

        