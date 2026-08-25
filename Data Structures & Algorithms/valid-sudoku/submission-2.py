class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # flattened box index

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_i = (r // 3) * 3 + (c // 3)  # flatten box coord to 0-8

                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_i]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_i].add(val)

        return True    