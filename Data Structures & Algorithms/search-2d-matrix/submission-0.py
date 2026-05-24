class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        n = len(matrix[0]) - 1 

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[mid][n] and target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][n]:
                left = mid + 1
            else:
                l = 0
                r = n
                while l <= r:
                    m = (l+r) // 2
                    if target < matrix[mid][m]:
                        r = m - 1
                    elif target > matrix[mid][m]:
                        l = m + 1
                    else:
                        return True
                return False

        return False

        