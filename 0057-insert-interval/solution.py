class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final_intervals = []
        i = 0
        n = len(intervals)
        
        # Phase I: find all intervals that end before start of `newInterval`
        while i < n and intervals[i][1] < newInterval[0]:
            final_intervals.append(intervals[i])
            i += 1

        # Phase II: find all intervals to merge with `newInterval`
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        final_intervals.append(newInterval)
        
        # Phase II: find all remaining intervals that start after the end of `newInterval`
        while i < n:
            final_intervals.append(intervals[i])
            i += 1

        return final_intervals