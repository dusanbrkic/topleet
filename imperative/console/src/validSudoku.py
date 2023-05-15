class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowMap = {}
        colMap = {}
        x3Map = {}
        for i in range(0, len(board)):
            for j in range (0, len(board[i])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rowMap.get(i, set()):
                    return False
                rowMap[i] = rowMap.get(i, set())
                rowMap[i].add(board[i][j])

                if board[i][j] in colMap.get(j, set()):
                    return False
                colMap[j] = colMap.get(j, set())
                colMap[j].add(board[i][j])

                if board[i][j] in x3Map.get((i//3, j//3), set()):
                    return False
                x3Map[(i//3, j//3)] = x3Map.get((i//3, j//3), set())
                x3Map[(i//3, j//3)].add(board[i][j])
        return True