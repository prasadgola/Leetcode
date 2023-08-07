class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_column = len(matrix[0])

        lowest_row, highest_row = 0, len(matrix) - 1

        while lowest_row <= highest_row:
            left, right = 0, total_column - 1
            row = (highest_row + lowest_row) // 2

            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if matrix[row][0] < target:
                lowest_row = row + 1
            else:
                highest_row = row - 1

        return False