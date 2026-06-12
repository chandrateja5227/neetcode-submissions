class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        left = 0
        right = len(matrix)-1
        l = 0
        r = len(matrix[0])-1
        while (left <= right):                
            mid = (right + left)//2

            if matrix[mid][0] <= target <= matrix[mid][r]:
                while l<=r:
                    m = (r + l )//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m+1
                    else:
                        r = m-1
                return False
            elif matrix[mid][r] < target:
                left = mid+1
            else:
                right = mid-1

        return False