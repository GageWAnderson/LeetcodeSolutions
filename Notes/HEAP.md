**BLUF:**
- Use a heap when you repeatedly need the min or max of a changing collection
- Python's `heapq` is a **min-heap** — negate values to simulate a max-heap
- The key operations are all O(log n); building from a list is O(n)

## Ask Yourself the Following
1. Do I need the K largest/smallest elements?
2. Do I need the global min/max repeatedly as the set changes?
3. Am I merging K sorted streams?
4. Am I tracking a running median (two-heap trick)?

## Python `heapq` Cheatsheet
```python
import heapq

heap = []
heapq.heappush(heap, val)       # O(log n)
val = heapq.heappop(heap)       # O(log n) — removes and returns smallest
val = heap[0]                   # O(1) — peek without removing
heapq.heapify(lst)              # O(n) — convert list in-place to min-heap

# Convenience (less common in interviews — prefer manual heap for control)
heapq.nsmallest(k, iterable)    # O(n log k)
heapq.nlargest(k, iterable)     # O(n log k)
```

**Max-heap:** negate every value on push/pop
```python
heapq.heappush(heap, -val)
val = -heapq.heappop(heap)
```

**Custom priority:** push tuples — heapq compares element by element
```python
heapq.heappush(heap, (priority, value))
priority, value = heapq.heappop(heap)
```

---

**Top-K Elements:**
- Maintain a min-heap of size K while iterating — the heap always holds the K largest seen so far
- Pop when size exceeds K (cheapest element falls off the bottom)

CANONICAL PROBLEMS:
- Kth Largest Element in an Array
- Top K Frequent Elements
- K Closest Points to Origin

MENTAL MODEL:
- "I want to keep the K best — use a min-heap as a bouncer: if the new element beats the worst keeper, swap it in"

NOTES:
- Heap of size K → O(n log K) time, O(K) space
- If K is close to n, just sort: O(n log n)
- If you need the actual Kth element (not the full top-K list), same approach — `heap[0]` at the end

TEMPLATE:
```python
heap = []
for val in nums:
    heapq.heappush(heap, val)
    if len(heap) > k:
        heapq.heappop(heap)   # evict the smallest — keeps K largest
# heap[0] is the Kth largest; list(heap) is the top-K (unsorted)
```

EXAMPLES:
- Kth Largest Element in an Array
```python
def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

- Top K Frequent Elements
```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    # min-heap on frequency; keeps K most frequent
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]
```

- K Closest Points to Origin
```python
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (-dist, x, y))  # max-heap on distance
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]
```

---

**K-Way Merge:**
- Merge K sorted lists by always popping the current global minimum
- Heap stores `(value, list_index, element_index)` — advance the pointer when you pop

CANONICAL PROBLEMS:
- Merge K Sorted Lists
- Smallest Range Covering Elements from K Lists
- Find K Pairs with Smallest Sums

MENTAL MODEL:
- "K sorted streams — keep one cursor per stream in the heap, always advance the winner"

TEMPLATE:
```python
heap = []
for i, lst in enumerate(lists):
    if lst:
        heapq.heappush(heap, (lst[0], i, 0))

result = []
while heap:
    val, i, j = heapq.heappop(heap)
    result.append(val)
    if j + 1 < len(lists[i]):
        heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
```

EXAMPLES:
- Merge K Sorted Lists (linked list version)
```python
def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = cur = ListNode(0)
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

---

**Two-Heap Median Trick:**
- Split the stream into a lower half (max-heap) and upper half (min-heap)
- Invariant: `len(lo) == len(hi)` or `len(lo) == len(hi) + 1`
- Median is `lo[0]` (odd total) or `(-lo[0] + hi[0]) / 2` (even total)

CANONICAL PROBLEMS:
- Find Median from Data Stream
- Sliding Window Median

MENTAL MODEL:
- "lo is a max-heap for the bottom half, hi is a min-heap for the top half — always rebalance after each insert"

TEMPLATE:
```python
lo = []   # max-heap (negate values)
hi = []   # min-heap

def add_num(num):
    heapq.heappush(lo, -num)          # always push to lo first
    heapq.heappush(hi, -heapq.heappop(lo))  # balance: push lo's max to hi
    if len(hi) > len(lo):             # keep lo >= hi in size
        heapq.heappush(lo, -heapq.heappop(hi))

def find_median():
    if len(lo) > len(hi):
        return -lo[0]
    return (-lo[0] + hi[0]) / 2
```

---

**Greedy Scheduling / Interval Problems:**
- Sort by start time, use a min-heap of end times to track active intervals
- Pop intervals that have already ended before adding the new one

CANONICAL PROBLEMS:
- Meeting Rooms II (minimum number of rooms)
- Task Scheduler
- Reorganize String

MENTAL MODEL:
- "Process events in order; heap tracks the earliest thing that frees up"

EXAMPLE:
- Meeting Rooms II
```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    intervals.sort()
    heap = []   # end times of active meetings
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)  # reuse the room that freed up
        else:
            heapq.heappush(heap, end)     # need a new room
    return len(heap)
```

---

**How to Choose Heap vs. Other Structures:**
- Need the single min/max of a *static* collection → just use `min()`/`max()`, O(n)
- Need repeated min/max as elements are added/removed → heap
- Need K-th element with no updates → quickselect, O(n) average
- Need sliding window min/max → monotonic deque (faster, O(n) total)
- Need sorted order for everything → just sort
