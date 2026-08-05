class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        count = Counter(tasks)

        waitingTasks = deque()
        heap = []
        for c in count.values():
            heap.append(0 - c)

        heapq.heapify(heap)

        while heap or waitingTasks:
            time += 1
            if heap:
                task = heapq.heappop(heap) + 1

                if task != 0:
                    waitingTasks.append((time + n, task))

            if not heap and waitingTasks:
                time = waitingTasks[0][0]

            if waitingTasks and waitingTasks[0][0] == time:
                readyTask = waitingTasks.popleft()
                heapq.heappush(heap, readyTask[1])

        return time
        