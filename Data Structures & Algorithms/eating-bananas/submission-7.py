import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxK = max(piles)

        left = 1
        right = maxK
        k = maxK
        while left <=right:
            mid = (left + right) // 2            
            if self.findK(mid,h,piles):
                k = min(k,mid)
                right = mid - 1
            else:
                left = mid + 1

        return k



    def findK(self,k,h,piles):
        hours = 0

        for p in piles:
            hours += math.ceil(p/k)

        return hours <= h






        