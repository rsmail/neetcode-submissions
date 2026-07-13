class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [val, timeStamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:    
            self.store[key] = []
        self.store[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        #we are looking for the largest timestamp val
        res = ""
        if key not in self.store:
            return res
        
        values = self.store[key]
        # values = [[val, timestamp], [val, timestamp], [val, timestamp]]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1

            else:
                r = m - 1


        return res
        
