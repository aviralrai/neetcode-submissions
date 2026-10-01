class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        R,C = len(grid),len(grid[0])
        island = 0
        for r in range(R):
            for c in range(C):
                if (r,c) in visited or grid[r][c] == "0":
                    continue
                island += 1
                visited.add((r,c))
                q = deque([(r,c)])
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr = cr + dr
                        nc = cc + dc
                        if nr >= 0 and nr < R and nc >= 0 and nc < C and (nr,nc) not in visited and grid[nr][nc] == "1":
                            visited.add((nr,nc))
                            q.append((nr,nc))
        return island

        