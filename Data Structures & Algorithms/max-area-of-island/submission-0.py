class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWs , COLs = len(grid) , len(grid[0])
        Visited = set()

        def dfs(grid, r, c, Visited):
            if not (0 <= r < ROWs and 0 <= c < COLs) or grid[r][c] == 0:
                return 0
            if (r,c) in Visited:
                return 0

            Visited.add((r,c))
            count = 1

            count +=  dfs(grid, r+1, c, Visited)
            count +=  dfs(grid, r-1, c, Visited)
            count +=  dfs(grid, r, c+1, Visited)
            count +=  dfs(grid, r, c-1, Visited)

            return count
        count = 0
        for i in range(ROWs):
            for j in range(COLs):
                if grid[i][j] == 1 and (i,j) not in Visited :
                    count = max(count,dfs(grid, i, j, Visited))

        return count

            
        