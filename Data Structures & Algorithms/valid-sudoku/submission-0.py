rows = [[(i, j) for j in range(9)] for i in range(9)]
cols = [[(i, j) for i in range(9)] for j in range(9)]
blocks = [
    [(i + di, j + dj) for di in (0, 1, 2) for dj in (0, 1, 2)]
    for i in (0, 3, 6)
    for j in (0, 3, 6)
]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(group):
            for ids in group:
                found = [False] * 10
                for i, j in ids:
                    val = board[i][j]
                    if val != ".":
                        val = int(val) - 1
                        if found[val]:
                            return False
                        found[val] = True
            return True
        return is_valid(rows) and is_valid(cols) and is_valid(blocks)
