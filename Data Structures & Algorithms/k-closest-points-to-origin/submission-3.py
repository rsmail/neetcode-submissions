class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i]
            dist = x**2 + y**2
            points[i] = [dist, x, y]
        heapq.heapify(points)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(points)
            res.append([x, y])
            k -= 1
        return res
            
        