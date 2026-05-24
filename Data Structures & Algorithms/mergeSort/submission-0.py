# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import math
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.merge(pairs,0,len(pairs)-1)
        return pairs

        
    def merge(self, pairs, start, end):
        if end - start + 1 <= 1:
            return

        m = (start + end) // 2
        self.merge(pairs, start, m)
        self.merge(pairs, m + 1, end)


        self.mergeFinal(pairs,start,m,end)

        return


    def mergeFinal(self,pairs,start,m,end):

        left = pairs[start : m+1]
        right = pairs[m+1 : end+1]

        i = 0
        j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i+=1
            else:
                pairs[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            pairs[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            pairs[k] = right[j]
            j+=1
            k+=1


    


        
