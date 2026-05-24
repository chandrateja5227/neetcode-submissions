class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows , cols = len(grid) , len(grid[0])
        visted = [[0 for i in range(cols)] for j in range(rows)]
        count = 0
        def dfs(grid,r,c,visted):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == '0':
                return
            if visted[r][c] == 1:
                return

            
            visted[r][c] = 1

            dfs(grid,r,c+1,visted)
            dfs(grid,r+1,c,visted)
            dfs(grid,r-1,c,visted)
            dfs(grid,r,c-1,visted)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and visted[r][c] == 0:
                    dfs(grid,r,c,visted)
                    count+=1

        return count