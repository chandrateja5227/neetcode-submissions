class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board[0]))]
        squares = [set() for i in range(len(board[0]))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                square = (row//3)*3+(col//3)
                if int(board[row][col]) not in range(1,10) or board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[square]:
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[square].add(board[row][col])

        return True


        