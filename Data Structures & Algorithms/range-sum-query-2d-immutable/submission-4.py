class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.prefixSum = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for row in range(len(matrix)):

            prefix = 0

            for col in range(len(matrix[0])):
                prefix += matrix[row][col]
                above = self.prefixSum[row][col+1]
                self.prefixSum[row+1][col+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.prefixSum[row2][col2]
        above = self.prefixSum[row1-1][col2]
        left = self.prefixSum[row2][col1-1]
        topLeft = self.prefixSum[row1-1][col1-1]

        result = bottomRight - above - left + topLeft

        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)