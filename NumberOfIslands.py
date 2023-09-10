class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       if not grid:
           return 0

        visit = set()
        islands = 0
        rw, cl = len(grid), len(grid[0])


        def bfs(r,c):
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            q = collections.deque()
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dl in directions:
                    if ((row+dr) in range(rw) and (col + dl) in range(cl) and (grid[row+dr,col+dw] == "1") and ((row+dr,col+dl) not in vist)):
                        q.append(row+dr,col+dr)
                        visit.add((row+dr,col+dr))


        for r in range(rw):
            for c in range(cl):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands