import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (-1 * distance, point))  # negate the distance (i.e., priority) since Python's heapq is min heap by default (maintaining smallest K requires max heap instead)
            if len(heap) > k:
                heapq.heappop(heap) # remove the element with the largest distance
        return [point for distance, point in heap]