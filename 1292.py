class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row = len(mat)
        column = len(mat[0])
        maxsidelenght = max(row, column)
        highboundside = maxsidelenght
        lowboundside = 0
        mid = (maxsidelenght + lowboundside) / 2
        for i in range(len(row - mid + 1)):
            for j in range(column - mid + 1):
                print(i, j)
