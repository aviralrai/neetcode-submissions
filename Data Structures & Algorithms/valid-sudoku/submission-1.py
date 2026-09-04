class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == ".":
                    continue
                if ele in rows[r] or ele in cols[c] or ele in squares[(r//3,c//3)]:
                    return False
                rows[r].add(ele)
                cols[c].add(ele)
                squares[(r//3,c//3)].add(ele)
        
        return True