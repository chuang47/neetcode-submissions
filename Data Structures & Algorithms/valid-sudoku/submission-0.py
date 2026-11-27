class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    n = int(board[i][j])
                    if n in seen or n in cols[j] or n in boxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    seen.add(n)
                    cols[j].add(n)
                    boxes[(i // 3) * 3 + (j // 3)].add(n)
        return True    
        




