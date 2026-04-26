**BLUF:**
- Use a stack when a future element needs to "resolve" waiting past elements (next greater, matching pairs)
- Mental model: stack = "things waiting for their answer" — pop when resolved
- Python's `list` is a stack: `append()` to push, `pop()` to pop, `[-1]` to peek

## Ask Yourself the Following
1. Am I matching pairs (parentheses, brackets)?
2. Am I finding the next or previous greater/smaller element?
3. Does a new element "resolve" or "invalidate" previous elements?
4. Do I need to backtrack or undo operations?

**Matching / Validation:**
- Push open brackets; on close, check if it matches the top
- A mismatch or empty stack on close means invalid

CANONICAL PROBLEMS:
- Valid Parentheses
- Decode String
- Basic Calculator

MENTAL MODEL:
- "Unresolved opens wait on the stack; each close resolves the most recent open"

TEMPLATE:
```python
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
for c in s:
    if c in '([{':
        stack.append(c)
    elif c in ')]}':
        if not stack or stack[-1] != pairs[c]:
            return False
        stack.pop()
return not stack
```

EXAMPLES:
- Valid Parentheses
```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return not stack
```

---

**Monotonic Stack (Next/Previous Greater or Smaller):**
- Maintain a stack in increasing or decreasing order
- When the current element breaks the order, pop and resolve waiting elements

CANONICAL PROBLEMS:
- Daily Temperatures
- Next Greater Element I / II
- Largest Rectangle in Histogram
- Trapping Rain Water

MENTAL MODEL:
- "Elements wait on the stack until something bigger (or smaller) arrives to resolve them"

NOTES:
- Decreasing stack → resolves "next greater element" (pop when you find something bigger)
- Increasing stack → resolves "next smaller element" (pop when you find something smaller)
- Store indices, not values, so you can compute distances and widths

TEMPLATE (next greater element):
```python
stack = []  # decreasing stack of indices
result = [-1] * len(nums)
for i, val in enumerate(nums):
    while stack and nums[stack[-1]] < val:
        result[stack.pop()] = val   # val is the next greater for stack top
    stack.append(i)
return result
```

EXAMPLES:
- Daily Temperatures
```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result
```

- Largest Rectangle in Histogram
```python
def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # increasing stack of indices
    max_area = 0
    heights.append(0)  # sentinel to flush remaining stack at end
    for i, h in enumerate(heights):
        start = i
        while stack and heights[stack[-1]] > h:
            idx = stack.pop()
            width = i - (stack[-1] + 1 if stack else 0)
            max_area = max(max_area, heights[idx] * width)
            start = idx
        stack.append(start)
    return max_area
```

---

**Undo / Simulation / State History:**
- Use a stack to track previous states when an operation needs to be reversed

CANONICAL PROBLEMS:
- Min Stack
- Evaluate Reverse Polish Notation
- Simplify Path

MENTAL MODEL:
- "Each frame is one level of context — push when entering, pop when leaving"

EXAMPLE:
- Min Stack
```python
class MinStack:
    def __init__(self):
        self.stack = []      # (value, current_min)

    def push(self, val):
        cur_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, cur_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]
```

- Evaluate Reverse Polish Notation
```python
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
           '*': lambda a, b: a * b, '/': lambda a, b: int(a / b)}
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[0]
```

---

**How to Choose Stack vs. Other Structures:**
- Need to resolve next/previous relationships → monotonic stack
- Need to match pairs or validate nesting → stack
- Need level-by-level processing → queue (BFS), not stack
- Need undo with O(1) min/max access → stack with augmented state (Min Stack pattern)
- Need the global minimum repeatedly from a changing set → heap
