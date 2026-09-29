class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-1*x for x in freq.values()]
        heapq.heapify(max_heap)
        q = deque()
        count = 0
        while max_heap or q:
            count += 1
            if not max_heap:
                count = q[0][1]
            else:
                c = heapq.heappop(max_heap)
                if c+1 < 0: q.append([c+1,count+n])
            if q and q[0][1] == count:
                fr,_ = q.popleft()
                heapq.heappush(max_heap,fr)
        return count


        