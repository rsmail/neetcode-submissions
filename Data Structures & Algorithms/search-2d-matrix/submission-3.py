class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:

                if self.search(matrix[i], target):
                    return True
            else:
                continue
        return False




    def search(self, array: List[int], target: int) -> bool:
        l, r = 0, len(array) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if array[mid] > target:
                r = mid - 1
            elif array[mid] < target:
                l = mid + 1
            else:
                return True
        return False
        