class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append([point[0]**2 + point[1]**2, point])
        heapq.heapify(distances)
        res = []
        n = 0
        while n < k:
            popped = heapq.heappop(distances)
            res.append(popped[1])
            n += 1
        return res