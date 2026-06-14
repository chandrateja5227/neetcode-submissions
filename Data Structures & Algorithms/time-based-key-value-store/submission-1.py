class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key , 0):
            arr = self.hashmap[key]
            arr.append((timestamp,value))
            self.hashmap[key] = arr
        else:
            self.hashmap[key] = [(timestamp,value)]

         
    def get(self, key: str, timestamp: int) -> str:
        if self.hashmap.get(key , 0):
            arr = self.hashmap[key]
            left = 0
            right = len(arr)-1
            target = -1
            while left <= right:
                mid = (left + right) //2
         
                if (arr[mid][0] == timestamp):
                    return arr[mid][1]

                if arr[mid][0] < timestamp:
                    target = mid
                    left = mid+1
                else:
                    right = mid-1

            return  arr[target][1] if target>=0 else ""             
        else:
            return ""


        
