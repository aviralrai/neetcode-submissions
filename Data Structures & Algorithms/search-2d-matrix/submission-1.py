class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)
        while lo < hi:
            mid_row = (lo+hi)//2
            # print(matrix[mid_row])
            if target <= matrix[mid_row][-1] and target >= matrix[mid_row][0]:
                # print("yes")
                lo_c, hi_c = 0, len(matrix[mid_row])
                while lo_c < hi_c:
                    mid_col = (lo_c + hi_c)//2
                    if matrix[mid_row][mid_col] < target:
                        lo_c = mid_col + 1
                    else:
                        hi_c = mid_col
                return True if lo_c < len(matrix[mid_row]) and matrix[mid_row][lo_c] == target else False
            elif target < matrix[mid_row][0]:
                hi = mid_row - 1
            else: lo = mid_row + 1
        if lo < len(matrix):
            # print(matrix[lo])
            lo_c, hi_c = 0, len(matrix[lo])
            while lo_c < hi_c:
                mid_col = (lo_c + hi_c)//2
                if matrix[lo][mid_col] < target:
                    lo_c = mid_col + 1
                else:
                    hi_c = mid_col
            return True if lo_c < len(matrix[lo]) and matrix[lo][lo_c] == target else False
        return False
        