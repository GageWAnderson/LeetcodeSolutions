**BLUF:**
- Use a queue when you process elements in arrival order or explore layer by layer
- BFS (level-order traversal, shortest path in unweighted graphs) is the dominant queue pattern
- For sliding window min/max, use a monotonic deque instead of a heap — O(n) vs O(n log k)

## Ask Yourself the Following
1. Am I finding the shortest path or minimum steps in an unweighted graph?
2. Am I processing a tree level by level?
3. Do I need the min or max of a sliding window efficiently?
4. Am I simulating arrival-order processing (scheduling, round-robin)?

**BFS — Shortest Path / Level Order:**
- Use a queue to explore all neighbors before going deeper
- Guarantees shortest path in unweighted graphs

CANONICAL PROBLEMS:
- Binary Tree Level Order Traversal
- Word Ladder
- Rotting Oranges
- Number of Islands (BFS version)

MENTAL MODEL:
- "Expand all nodes at distance d before any at distance d+1 — the first time you reach a node is the shortest path"

NOTES:
- Always mark visited *before* enqueuing (not after dequeuing) to avoid duplicate processing
- Level-order: snapshot `len(queue)` at the start of each layer to process one level at a time
- BFS works on implicit graphs (grids, word transformations) — model nodes/edges abstractly

TEMPLATE (shortest path):
```python
from collections import deque

queue = deque([start])
visited = {start}
steps = 0
while queue:
    for _ in range(len(queue)):   # process one level at a time
        node = queue.popleft()
        if node == target:
            return steps
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    steps += 1
return -1  # unreachable
```

EXAMPLES:
- Binary Tree Level Order Traversal
```python
def level_order(root) -> list[list[int]]:
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

- Rotting Oranges (multi-source BFS — start from all rotten oranges simultaneously)
```python
def oranges_rotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while queue and fresh:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
```

---

**Monotonic Deque (Sliding Window Min/Max):**
- Maintain a deque of indices in decreasing order (for max) or increasing order (for min)
- Front is always the current window's answer; evict dominated elements from the back

CANONICAL PROBLEMS:
- Sliding Window Maximum
- Shortest Subarray with Sum at Least K

MENTAL MODEL:
- "Evict useless candidates from the back — they can never be the answer while a better element exists inside the window"

NOTES:
- O(n) total — each element enters and leaves the deque at most once
- Store indices (not values) so you can check whether elements have left the window
- Decreasing deque → window max; increasing deque → window min

TEMPLATE (sliding window maximum):
```python
from collections import deque

dq = deque()  # decreasing deque of indices
result = []
for i, val in enumerate(nums):
    while dq and nums[dq[-1]] <= val:
        dq.pop()                     # remove dominated elements from back
    dq.append(i)
    if dq[0] < i - k + 1:
        dq.popleft()                 # remove elements that left the window
    if i >= k - 1:
        result.append(nums[dq[0]])   # front is always the window max
return result
```

EXAMPLES:
- Sliding Window Maximum
```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()
    result = []
    for i, val in enumerate(nums):
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        dq.append(i)
        if dq[0] < i - k + 1:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

---

**Simulation / Scheduling:**
- FIFO processing: first in, first out order matters for correctness

CANONICAL PROBLEMS:
- Number of Recent Calls
- Design Hit Counter
- Task Scheduler (combine with max-heap for greedy frequency tracking)

MENTAL MODEL:
- "Who arrived first gets processed first — the queue preserves that order"

EXAMPLE:
- Number of Recent Calls
```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```

---

**How to Choose Queue vs. Other Structures:**
- Shortest path / level-by-level exploration → BFS with queue
- Sliding window min/max → monotonic deque, O(n) total vs heap O(n log k)
- Need overall min/max of a changing set → heap
- Next/previous relationships between elements → stack
- Process elements in sorted priority order → heap / priority queue
