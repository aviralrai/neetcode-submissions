class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        R = len(grid)
        C = len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        if fresh == 0:
            return 0
        mins = 0
        c = 0
        while q:
            if fresh == 0:
                return mins
            mins += 1
            curr = len(q)
            for i in range(curr):
                cc, cr = q.popleft()
                for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nr = cr + dr
                    nc = dc + cc
                    if nr >= 0 and nc >= 0 and nr < R and nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
        return -1

        