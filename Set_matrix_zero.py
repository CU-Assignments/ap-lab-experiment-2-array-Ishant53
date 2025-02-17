from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use the first row and column to mark zeroes
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the first column of the row
                    matrix[0][j] = 0  # Mark the first row of the column

        # Set zeroes based on the markers in the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle the first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle the first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


# Example usage
solution = Solution()
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
solution.setZeroes(matrix)
print(matrix)