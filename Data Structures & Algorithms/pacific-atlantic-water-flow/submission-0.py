class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        P = set()
        A = set()
        R = len(heights)
        C = len(heights[0])
        P.update((r,0) for r in range(R))
        P.update((0,c) for c in range(C))
        A.update((r,C-1) for r in range(R))
        A.update((R-1,c) for c in range(C))
        q = deque(cell for cell in P)
        while q:
            r,c = q.popleft()
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if nr >=0 and nr < R and nc >= 0 and nc < C and (nr, nc) not in P and heights[nr][nc] >= heights[r][c]:
                    q.append((nr,nc))
                    P.add((nr,nc))
        a_q = deque((r,c) for r,c in A)
        while a_q:
            r,c = a_q.popleft()
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if nr >=0 and nr < R and nc >= 0 and nc < C and (nr, nc) not in A and heights[nr][nc] >= heights[r][c]:
                    a_q.append((nr,nc))
                    A.add((nr,nc))
        res = A.intersection(P)
        res_list = [list(item) for item in res]
        return res_list

        