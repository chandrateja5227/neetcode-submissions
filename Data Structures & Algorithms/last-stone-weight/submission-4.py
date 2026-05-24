import heapq
class Solution:


    def lastStoneWeight(self, stones: List[int]) -> int:
        if not len(stones):
            return 0
        if len(stones) == 1:
            return stones[0]
    
        arr = [-x for x in stones]
        heapq.heapify(arr)
  

        while len(arr) >= 2:
            i = heapq.heappop(arr)
            j = heapq.heappop(arr)
            if i == j:
                continue
            elif i < j:
                heapq.heappush(arr,i-j)
            else:
                heapq.heappush(arr,j-i)


        return -arr[0] if len(arr) else 0