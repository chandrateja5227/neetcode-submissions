class TimeMap:

    def __init__(self):
        self.hashmap ={None : []}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value,timestamp))
        else:
            self.hashmap[key] = [(value,timestamp)]

            

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashmap:
            return ""

        if len(self.hashmap[key]) == 1:
            return self.hashmap[key][0][0] if self.hashmap[key][0][1] <= timestamp else ""

        else:
            return self.binarySearch(self.hashmap[key] , timestamp)






    def binarySearch(self, arr, timestamp):
        left = 0
        right = len(arr)-1
        result = ""
        while left <= right:
            mid = (left+right) // 2

            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                left = mid+1
            else:
                right = mid-1 

        return result


        
