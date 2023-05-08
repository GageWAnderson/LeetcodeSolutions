from functools import lru_cache

# @lru_cache annoation does the work of memoizing a function often called
# With the same arguments for you - useful to know, but don't use in an interview


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    n = 100
    print(fibonacci(n))