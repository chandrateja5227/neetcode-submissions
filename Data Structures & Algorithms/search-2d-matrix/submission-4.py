class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix)-1
        n = len(matrix[0])
        while left <= right:

            mid = (left+right)//2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                l = 0
                r = n-1
                while l<=r:
                    m = (l+r)//2
                    if matrix[mid][m] == target:
                        return True
                    if matrix[mid][m] < target:
                        l=m+1
                    else:
                        r=m-1
                return False

            if matrix[mid][n-1] < target:
                left = mid+1
            else:
                right = mid-1

        return False


        