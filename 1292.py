class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        row = len(mat)
        column = len(mat[0])
        maxsidelenght = min(row, column)
        highboundside = maxsidelenght
        lowboundside = 0
        # mid = (maxsidelenght + lowboundside) // 2
        # mid = mid + 1 if mid < 2 else mid
        mid = 2
        
        while mid > 1:
	        for i in range(row - mid + 1):
	        	for j in range(column - mid + 1):
	        		print(i, j)
	        		total = 0
	        		for i in range(mid):
	        			print(mat[i][j:j+mid])
	        			total += sum(mat[i][j:j+mid])
	        			print(total)
	        		if total < threshold:
	        			print(mid)
	        			return 0




solution = Solution()
solution.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)





