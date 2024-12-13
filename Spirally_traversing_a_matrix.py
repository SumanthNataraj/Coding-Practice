"""You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form."""
def spirallyTraverse(self, matrix):
    
        # Initialize variables and result list  for spiral traversal
        
        m = len(matrix)
        n = len(matrix[0])
        result = []
        top = 0
        down = m - 1
        left = 0
        right = n - 1
        dir = 0
    
        while top <= down and left <= right:
            if dir == 0:  # Left to Right
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
            elif dir == 1:  # Top to Bottom
                for i in range(top, down + 1):
                    result.append(matrix[i][right])
                right -= 1
            elif dir == 2:  # Right to Left
                for i in range(right, left - 1, -1):
                    result.append(matrix[down][i])
                down -= 1
            elif dir == 3:  # Bottom to Top
                for i in range(down, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
            dir = (dir + 1) % 4  # Cycle direction
        
        return result

# Test the function

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(spirallyTraverse(matrix))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]