**BLUF:**
- Avoids O(n^2) on string and array problems by re-using previous work
- Instead of restarting to find new solutions, you intelligently re-use previous work by moving pointers intelligently
- Use `for` loops when the advancement of a pointer (often j) is garunteed, use a whiile loop when pointer advancement is conditional

## Ask Yourself the Following
1. What do my pointers represent?
  a. pair?
  b. Window?
  c. Traversal Speed?
2. What invariant am I maintaining?
  a. Sum <= target?
  b. No duplicates?
  c. Pointers converging?

**Opposite Ends Classic Two Pointers Problem:**
- Two pointers start at both ends of an array and eliminate search space
- Pointers don't have a predictable advancement pattern (for loop) but 1 moves per step (while loop)

CANONICAL PROBLEMS:
- Two Sum II
- Container with Most Water
- Valid Palindrome
- 3Sum (after fixing one index to turn into a two pointers problem)

MENTAL MODEL:
- "I can discard half the possibilities at each step"
- i.e if the sum is too large move a pointer right, else move it left

NOTES:
- Best used when array inputs are sorted
- Best when you're looking for pairs (sum, difference, etc)
- Symmetry (i.e Palindromes)
- Often allow for greedy elimination of search space

TEMPLATE:
```python
l, r = 0, len(arr) - 1
while l < r:
    if found(arr[l], arr[r]):
        l += 1; r -= 1
    elif need_larger(arr[l], arr[r]):
        l += 1
    else:
        r -= 1
```

EXAMPLES:
- Two Sum II (sorted input → pair that sums to target)
```python
def two_sum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
```

- Valid Palindrome (skip non-alphanumeric, case-insensitive)
```python
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while l < r and not s[r].isalnum(): r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1; r -= 1
    return True
```

- Container With Most Water (greedy: always move the shorter side)
```python
def max_area(height: list[int]) -> int:
    l, r, res = 0, len(height) - 1, 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res
```

**Fast/Slow Pointers Problem:**
- Two pointers move at different speeds
- Use on linked lists, cycle detection, finding middle nodes, cycle entries, intersections

CANONICAL PROBLEMS:
- Linked list cycle
- Find middle of a linked list
- Happy number (cycle in a sequence)

MENTAL MODEL:
- If there's a loop, fast will eventually loop slow
- Distance shrinks modulo cycle length

NOTES:
- Not about searching, but detecting structure in a traversal

TEMPLATE:
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:  # cycle detected
        break
```

EXAMPLES:
- Linked List Cycle Detection
```python
def has_cycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

- Find Middle of Linked List (slow stops at middle when fast exhausts)
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

- Read/Write Pointer — Remove Duplicates from Sorted Array
```python
def remove_duplicates(nums: list[int]) -> int:
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

**Sliding Window (Same Direction Two Pointers):**
- Two pointers define a contiguous window (left, right) that grows and shrinks
- Use on sub-arrays and sub-strings
- Use when we care about everything inside the window (sum, freq_map, etc.)
  - Side note that `freq_map` or `bag` comes up a lot as part of sliding window solutions
- You're optimizing longest/shortest/max/in
- Pointers have a predictable advancement pattern (for loop) so moving j in a for loop makes most sense

CANONICAL PROBLEMS:
- Longest Substring without repeating characters
- Minimum window substring
- Max consecutive ones
- Subarray sum >= target

TEMPLATE (variable-size window — shrink while window is invalid):
```python
l = 0
state = ...  # sum, freq_map, count, etc.
res = 0
for r in range(len(arr)):
    # expand: add arr[r] to state
    while window_invalid(state):
        # shrink: remove arr[l] from state
        l += 1
    res = max(res, r - l + 1)  # or min, or accumulate
return res
```

TEMPLATE (fixed-size window — slide by one each step):
```python
window = sum(nums[:k])
res = window
for r in range(k, len(nums)):
    window += nums[r] - nums[r - k]
    res = max(res, window)
return res
```

EXAMPLES:
- Longest Substring Without Repeating Characters
```python
def length_of_longest_substring(s: str) -> int:
    seen = {}
    l = res = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l:
            l = seen[c] + 1
        seen[c] = r
        res = max(res, r - l + 1)
    return res
```

- Minimum Window Substring (freq_map pattern)
```python
def min_window(s: str, t: str) -> str:
    need = Counter(t)
    missing = len(t)
    l = res_l = res_r = 0
    for r, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if missing == 0:
            while need[s[l]] < 0:
                need[s[l]] += 1
                l += 1
            if not res_r or r - l < res_r - res_l:
                res_l, res_r = l, r
            need[s[l]] += 1
            missing += 1
            l += 1
    return s[res_l:res_r]
```

- Minimum Size Subarray Sum >= target (shrink while valid to minimize)
```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    l = total = 0
    res = float('inf')
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return res if res != float('inf') else 0
```

**How to Choose between Opposite Ends and Sliding Window:**
- Do I care about the contents between the pointers?
  - If yes, then sliding window
  - If no, then opposite ends
