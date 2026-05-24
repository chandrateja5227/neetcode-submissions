# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        if not pairs:
            return []
        self.sort(pairs, 0, len(pairs)-1)
        return pairs

    def sort(self, pairs, start, end):
        if end - start + 1 <= 1:
            return

        k = start

        for i in range(start,end):
            if pairs[i].key < pairs[end].key:
                temp =  pairs[i]
                pairs[i] = pairs[k]
                pairs[k] = temp
                k+=1

        temp =  pairs[k]
        pairs[k] = pairs[end]
        pairs[end] = temp


        self.sort(pairs, start, k-1 )
        self.sort(pairs, k+1, end)




        