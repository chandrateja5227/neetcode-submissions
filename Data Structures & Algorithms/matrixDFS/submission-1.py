class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        ROWS , COLS = len(grid) , len(grid[0])
        Visited = set()

        def dfs(grid, r, c, Visited):
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] == 1 :
                return 0
            if (r, c) in Visited:  
                return 0
            if r == ROWS - 1 and c == COLS -1:
                return 1

            Visited.add((r,c))

            count = 0
            count += dfs(grid, r+1, c, Visited)  
            count += dfs(grid, r, c+1, Visited) 
            count += dfs(grid, r-1, c, Visited)  
            count += dfs(grid, r, c-1, Visited)  
            Visited.remove((r,c)) 

            return count
        return dfs(grid, 0, 0, Visited)




                  