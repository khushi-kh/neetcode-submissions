class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        # checking in row
        for i in range(rows):

            seen_r = set()

            for j in range(cols):

                val = board[i][j]

                if val == ".": continue

                if val not in seen_r:
                    seen_r.add(val)
                else:
                    return False

        # checking in col
        for i in range(rows):

            seen_c = set()

            for j in range(cols):

                val = board[j][i]

                if val == ".": continue

                if val not in seen_c:
                    seen_c.add(val)
                else:
                    return False

        # checking in block

        for r in range(0,9,3):
            for c in range(0,9,3):

                seen_b = set()

                for i in range(3):
                    for j in range(3):

                        val = board[r+i][c+j]

                        if val == ".": continue

                        if val not in seen_b:
                            seen_b.add(val)
                        else:
                            return False

        return True

