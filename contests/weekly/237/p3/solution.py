from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_by_enqueue_time, tasks_by_processing_time = [], []
        for i, task in enumerate(tasks):
            heapq.heappush(tasks_by_enqueue_time, (task[0], i, task[1]))

        def getAvailableTasksAtTime(time: int) -> None:
            while tasks_by_enqueue_time and tasks_by_enqueue_time[0][0] <= time:
                t = heapq.heappop(tasks_by_enqueue_time)
                heapq.heappush(tasks_by_processing_time, (t[2], t[1]))

        results = []

        current_time = tasks_by_enqueue_time[0][0]
        while tasks_by_enqueue_time or tasks_by_processing_time:
            getAvailableTasksAtTime(current_time)

            if not tasks_by_processing_time:
                getAvailableTasksAtTime(tasks_by_enqueue_time[0][0])

            fastest = tasks_by_processing_time[0][0]
            temp = []
            while tasks_by_processing_time and tasks_by_processing_time[0][0] <= fastest:
                t = heapq.heappop(tasks_by_processing_time)
                heapq.heappush(temp, t[1])

            results.append(heapq.heappop(temp))
            current_time += fastest
            while temp:
                i = heapq.heappop(temp)
                heapq.heappush(tasks_by_processing_time, (fastest, i))

        return results


if __name__ == "__main__":
    test_cases = [
        (
            [[1, 2], [2, 4], [3, 2], [4, 1]],
            [0, 2, 3, 1]
        ),
        (
            [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]],
            [4, 3, 2, 0, 1]
        ),
        (
            [[100, 100], [1000000000, 1000000000]],
            [0, 1]
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.getOrder(t[0])
        if res != t[1]:
            sol.getOrder(t[0])
