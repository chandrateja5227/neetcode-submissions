class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        
        ROWS , COLS = len(grid) , len(grid[0])

        queue = deque()

        queue.append((0,0))
        
        Visited = set()
        Visited.add((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                row , col = queue.popleft()
                
                if row == (ROWS - 1) and col == (COLS -1):
                    return length

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for r , c in directions:
                    if not ( 0 <= (row + r) < ROWS and 0 <= (col + c) < COLS ) or (row + r , col + c) in Visited or grid[row + r][col + c] == 1:
                        continue
                    queue.append(((row + r) ,(col + c)))
                    Visited.add(((row + r),(col + c)))
                    
            length += 1
        return -1
        