class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            column = []
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in column:
                        return False
                    else:
                        column.append(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in row:
                        return False
                    else:
                        row.append(board[j][i])
        for x in range(3):
            for i in range(3):
                square = []
                for j in range(3):
                    for k in range(3):
                        value = board[j + 3*x][k + 3*i]
                        if value != '.':
                            if value in square:
                                return False
                            else:
                                square.append(value)
        return True