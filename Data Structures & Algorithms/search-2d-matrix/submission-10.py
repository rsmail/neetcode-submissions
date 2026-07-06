class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #two binary searches here. first the rows, then the cols
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break
        if not (top <= bot):
            return False
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[m][mid] < target:
                l = mid + 1
            elif matrix[m][mid] > target:
                r = mid -1
            else:
                return True
        return False

        