**BLUF:**
- Binary search is NOT just for sorted arrays — it's for any space with a monotonic yes/no condition
- You are eliminating half the search space each step, achieving O(log n) instead of O(n)
- Three patterns: exact search, boundary search, search on answer

## Ask Yourself the Following
1. Is there a sorted structure I'm searching?
2. Is there a condition where "if X works, everything larger/smaller also works"?
3. Am I minimizing/maximizing a value subject to a feasibility constraint?
4. Am I searching values or searching a *possibility space*?

**Classic Binary Search (Exact Value):**
- Search for a target in a sorted array
- Eliminate left or right half based on comparison with mid

CANONICAL PROBLEMS:
- Binary Search
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

MENTAL MODEL:
- "Each step cuts the world in half — always ask: can I rule out this entire side?"

NOTES:
- Use `l + (r - l) // 2` to avoid integer overflow (matters in other languages)
- `while l <= r` with `l = mid + 1` / `r = mid - 1` for exact search
- `while l < r` with `l = mid + 1` / `r = mid` for boundary search (see below)

TEMPLATE:
```python
l, r = 0, len(nums) - 1
while l <= r:
    mid = l + (r - l) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
return -1
```

EXAMPLES:
- Binary Search
```python
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

- Find Minimum in Rotated Sorted Array
```python
def find_min(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:
            l = mid + 1   # min is in the right half
        else:
            r = mid       # mid could be the min
    return nums[l]
```

---

**Boundary Search (Leftmost / Rightmost):**
- Find the first or last position satisfying a condition
- Use `l < r` and never exclude `mid` from the valid range

CANONICAL PROBLEMS:
- Find First and Last Position of Element in Sorted Array
- Search Insert Position

MENTAL MODEL:
- "I want the boundary of a yes/no region — shrink toward it without jumping past"

NOTES:
- Leftmost: `r = mid` when condition holds (don't exclude mid)
- Rightmost: `l = mid` when condition holds — use `mid = l + (r - l + 1) // 2` to avoid infinite loop

TEMPLATE (leftmost):
```python
l, r = 0, len(nums) - 1
while l < r:
    mid = l + (r - l) // 2
    if condition(nums[mid]):
        r = mid        # mid could be the answer, keep it
    else:
        l = mid + 1
return l
```

TEMPLATE (rightmost):
```python
l, r = 0, len(nums) - 1
while l < r:
    mid = l + (r - l + 1) // 2  # bias toward right to avoid infinite loop
    if condition(nums[mid]):
        l = mid        # mid could be the answer, keep it
    else:
        r = mid - 1
return l
```

---

**Binary Search on Answer (Search on Value Space):**
- You're not searching an array — you're searching the *range of possible answers*
- Define a feasibility function: "can we achieve answer X?"
- Find the minimum/maximum X where feasibility flips

CANONICAL PROBLEMS:
- Koko Eating Bananas
- Capacity To Ship Packages Within D Days
- Minimum Number of Days to Make m Bouquets

MENTAL MODEL:
- "The answer lives in some range [lo, hi]. Feasibility is monotonic — binary search that range."

NOTES:
- The key insight: if eating speed k works, then k+1 also works → monotonic → binary search
- Define `feasible(mid)` cleanly first, then wrap it in the binary search loop
- Set bounds carefully: lo = minimum possible answer, hi = maximum possible answer

TEMPLATE:
```python
def feasible(mid) -> bool:
    ...  # can we achieve the goal with value = mid?

lo, hi = min_possible, max_possible
while lo < hi:
    mid = lo + (hi - lo) // 2
    if feasible(mid):
        hi = mid       # mid works, try smaller
    else:
        lo = mid + 1   # mid doesn't work, need larger
return lo
```

EXAMPLES:
- Koko Eating Bananas
```python
def min_eating_speed(piles: list[int], h: int) -> int:
    def feasible(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

- Capacity to Ship Packages Within D Days
```python
def ship_within_days(weights: list[int], days: int) -> int:
    def feasible(cap):
        needed, cur = 1, 0
        for w in weights:
            if cur + w > cap:
                needed += 1
                cur = 0
            cur += w
        return needed <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

**How to Choose Binary Search vs. Other Patterns:**
- Sorted structure, looking for exact value → classic binary search
- Sorted structure, looking for first/last position → boundary search
- Optimizing a numeric answer with a monotonic feasibility condition → search on answer
- Need to repeatedly find min/max of a changing set → heap (not binary search)
- Linear scan suffices → don't add binary search complexity
