class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k = max(piles)
        left = 1
        right = k
        min = h
        while left <= right:
            mid = (left + right) // 2
            hours = self.check(mid,piles)
            if hours <= h:
                if k > mid:                   
                    k = mid
                right = mid - 1
            else:
                left = mid + 1


        return k
                 


    def check(self,m,piles):
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i]/m)
        
        return hours

        