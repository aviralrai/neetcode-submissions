class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        R, C = len(grid), len(grid[0])
        max_area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0 or (r,c) in visited:
                    continue
                area = 1
                q = deque([(r,c)])
                visited.add((r, c))
                while q:
                    cr, cc = q.popleft()
                    for dr,dc in [(-1,0),(0,-1),(0,1),(1,0)]:
                        nr, nc = dr+cr, dc+cc
                        if nr >= 0 and nr < R and nc >= 0 and nc < C and (nr,nc) not in visited and grid[nr][nc] == 1:
                            area += 1
                            visited.add((nr,nc))
                            q.append((nr,nc))
                max_area = max(max_area,area)
        return max_area
        