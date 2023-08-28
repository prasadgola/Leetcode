class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            d = x**2  + y**2
            heapq.heappush(minheap,[d, x, y])

        res = []
        while k > 0:
            dis, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k -= 1

        return res