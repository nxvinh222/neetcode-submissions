class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        found = False
        while left <= right:
            mid = left + (right - left) // 2

            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                found = True
                break

        if not found:
            return False

        row = matrix[mid]
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if target > row[mid]:
                left = mid + 1
            elif target < row[mid]:
                right = mid - 1
            else:
                return True

        return False
        