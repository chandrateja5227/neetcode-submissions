from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        
        ROWS , COLS = len(grid) , len(grid[0])

        queue = deque()

        queue.append((0,0))
        
        Visited = set()
        Visited.add((0,0))
        length = 1
        while queue:
            for i in range(len(queue)):
                row , col = queue.popleft()
                
                if row == (ROWS - 1) and col == (COLS -1):
                    return length

                directions = [
                            (-1, -1), (-1, 0), (-1, 1), # Top row
                            (0, -1),           (0, 1),  # Middle row (skip self)
                            (1, -1),  (1, 0),  (1, 1)   # Bottom row
                        ]
                for r , c in directions:
                    if not ( 0 <= (row + r) < ROWS and 0 <= (col + c) < COLS ) or (row + r , col + c) in Visited or grid[row + r][col + c] == 1:
                        continue
                    queue.append(((row + r) ,(col + c)))
                    Visited.add(((row + r),(col + c)))
                    
            length += 1
        return -1
                        
                        









        