class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        state = []
        if len(pairs):
            state.append(list(pairs))
        for i in range(1,len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:                              
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp
                j -= 1
           
            state.append(list(pairs))

        return state