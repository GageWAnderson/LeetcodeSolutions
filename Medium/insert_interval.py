class Solution:
    # NOTE: While loops are cleaner than for loops when we iterate through the array in multiple "phases"
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


class MySolution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        ans = []

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        if i >= len(intervals):
            ans.append(newInterval)
            return ans

        if newInterval[1] >= intervals[i][0]:
            merged_lower_bound = min(intervals[i][0], newInterval[0])
            merged_upper_bound = max(intervals[i][1], newInterval[1])

            while i < len(intervals) and intervals[i][0] <= merged_upper_bound:
                merged_upper_bound = max(intervals[i][1], newInterval[1])
                i += 1
            ans.append([merged_lower_bound, merged_upper_bound])
        else:
            ans.append(newInterval)

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans


class SolutionIncorrect:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # left, left_num = self.binary_search_leq(newInterval[0], intervals)
        # right, right_num = self.binary_search_greater(newInterval[1], intervals)

        if len(intervals) == 0:
            return [newInterval]

        left, left_num = self.find_left_bound_of_new_interval(newInterval[0], intervals)
        right, right_num = self.find_right_bound_of_new_interval(
            newInterval[1], intervals
        )

        ans = []
        if not left:
            ans = intervals
            ans.append(newInterval)
            return ans
        elif not right:
            ans.append(newInterval)
            for interval in intervals:
                ans.append(interval)
            return ans
        else:
            for interval in intervals[:left]:
                ans.append(interval)
            ans.append([left_num, right_num])
            if right + 1 < len(intervals) - 1:
                for interval in intervals[right + 1 :]:
                    ans.append(intervals[right:])
            return ans

    def find_left_bound_of_new_interval(
        self, start_of_new_interval: int, intervals: List[List[int]]
    ) -> Tuple[int, int] | None:
        # NOTE: O(n) linear search time
        for i in range(len(intervals)):
            if intervals[i][1] >= start_of_new_interval:
                return (i, intervals[i][0])
        return None  # If no left bound found, then append answer on end

    def find_right_bound_of_new_interval(
        self, new_interval: int, intervals: List[List[int]]
    ) -> Tuple[int, int] | None:
        for j in range(len(intervals)):
            if (
                intervals[j][0] <= new_interval[1]
                and intervals[j][1] >= start_of_new_interval
            ):
                return (j, intervals[j][1])
        return None

    # TODO: Is there a way to get the boundaries in O(logn) time?
    def binary_search_leq(
        self, new_interval_start: int, intervals: List[List[int]]
    ) -> Tuple[int, int]:
        """Find the index (left) in intervals where start of the
        new_interval_start is leq the end of the interval"""
        i = 0
        j = len(intervals) - 1
        while i < j:
            mid = i + (j - i) // 2
            if new_interval_start <= intervals[mid][1]:
                return (mid, intervals[mid])
            elif new_interval_start > intervals[mid]:
                i = mid
            else:
                j = mid

    def binary_search_geq(self, n: int, intervals: List[List[int]]) -> Tuple[int, int]:
        """Find the index (right) in intervals where end of the
        new_interval_start is geq the end of the interval"""
        pass
