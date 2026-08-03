class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][0] < target:
                top = row + 1
            else:
                break
        l, r = 0, COL - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
        