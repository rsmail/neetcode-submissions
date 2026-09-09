class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #turn list of [xi, yi] into list of [dist, xi, yi]
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = x ** 2 + y ** 2
            points[i] = [dist, x, y]
        heapq.heapify(points)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(points)
            k -= 1
            res.append([x, y])
        return res
        