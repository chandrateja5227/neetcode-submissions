class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        sortedpiles = sorted(piles)
        
        minK = sortedpiles[-1]

        left = 1
        right = sortedpiles[-1]


        while(left <= right):
            mid = (left + right)//2
            
            if mid == 0:
                left = 1
                continue

            total_hours = sum(math.ceil(p / mid) for p in piles)
            if total_hours <= h:
                minK = min(minK ,mid)
                right = mid-1
            else:
                left = mid+1

        return minK