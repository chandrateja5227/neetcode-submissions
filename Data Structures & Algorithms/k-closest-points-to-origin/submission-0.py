import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        arr = []
        for list in points:
            t = (math.sqrt((list[0] - 0)**2 + (list[1] - 0)**2) , list)
            arr.append(t)

        heapq.heapify(arr)

        return [heapq.heappop(arr)[1] for i in range(k)]
        