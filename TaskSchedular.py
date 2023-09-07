class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        


        while q or maxHeap:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append([c,time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time