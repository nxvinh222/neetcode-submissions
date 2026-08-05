class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        for index in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (index // 3) * 3 + i
                    col = (index % 3) * 3 + j

                    if board[row][col] == ".":
                        continue

                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])

        return True
        