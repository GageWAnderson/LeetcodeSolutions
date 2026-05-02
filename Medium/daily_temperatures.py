class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # NOTE: Sorting doesn't work since that will corrupt the data
        # That rules out binary search and most likely a two pointers approach
        # NOTE: Brute force is very easy, but how do we do better than O(n^2)?

        # How do we "know" what the warmest days are ahead without linear/binary search?
        # Can we use some type of data structure to track this?
        # How do we track an ordered set of all the temperatures ahead of each point?
        # My first thought is a heap, since the heap invariant will keep all the warmer temps on top
        # However, push/pop from the heap is O(logn), can we do better?
        # Heap wouldn't work since I need to search for both index and temperature?
        # "Give me the closest index to the right where the temperature greater than the current day"
        ans = [0 for _ in range(len(temperatures))]

        stack: List[Tuple[int, int]] = []  # Monotonic increasing top-to-bottom

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temperatures[i]))
        return ans


class SolutionIncorrect:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # NOTE: Sorting doesn't work since that will corrupt the data
        # That rules out binary search and most likely a two pointers approach
        # NOTE: Brute force is very easy, but how do we do better than O(n^2)?

        # How do we "know" what the warmest days are ahead without linear/binary search?
        # Can we use some type of data structure to track this?
        # How do we track an ordered set of all the temperatures ahead of each point?
        # My first thought is a heap, since the heap invariant will keep all the warmer temps on top
        # However, push/pop from the heap is O(logn), can we do better?
        # Heap wouldn't work since I need to search for both index and temperature?
        # "Give me the closest index to the right where the temperature greater than the current day"
        if len(temperatures) == 1:
            return [0]
        greatest_temps_stack = self.build_monotonic_stack(temperatures)
        ans = []
        for i, temp in enumerate(temperatures):
            if not greatest_temps_stack:
                ans.append(0)
            elif temp >= greatest_temps_stack[0][0]:
                while greatest_temps_stack and greatest_temps_stack[0][0] < temp:
                    greatest_temps_stack.pop()
                num_days = greatest_temps_stack[0][1] - i if greatest_temps_stack else 0
                ans.append(num_days)
            else:
                num_days = greatest_temps_stack[0][1] - i
                ans.append(num_days)

        return ans

    def build_monotonic_stack(self, temperatures: List[int]):
        """Builds a stack of the greatest temperatures at a given point in the temperature array"""
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack.pop()
            stack.append((temp, i))
        return stack
