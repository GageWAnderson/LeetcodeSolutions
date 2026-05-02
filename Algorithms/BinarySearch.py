class BinarySearch:  # Finds x in a SORTED array A
    def binSearch(self, A, x):
        n = len(A) - 1  # Don't forget the -1, common bug
        if n == 0:
            raise Exception("Array must contain some elements")

        l, r = 0, n

        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] == x:
                return True
            elif A[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False

    # NOTE: Finds the insert position on the right without disrupting elements that are already there
    # # NOTE: This variant of binary search reduces to 2 statements in if-else clause since if A[mid] == target, i could still be on the right of the target
    def binSearchRightmost(
        self, A, x
    ):  # Finds the rightmost occurence of x in a SORTED array A
        n = len(A)
        if n == 0:
            raise Exception("Array must contain some elements")

        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2
            if A[mid] > x:
                r = mid - 1
            else:
                l = mid
        return A[r - 1] == x

    # NOTE: Finds the insert position on the left of a sequence of the same nums without disrupting elements that are already there
    # NOTE: This variant of binary search reduces to 2 statements in if-else clause since if A[mid] == target, i could still be on the left of the target
    def binSearchLeftmost(
        self, A, x
    ):  # Finds the leftmost occurence of x in a SORTED array A
        n = len(A)
        if n == 0:
            raise Exception("Array must contain some elements")

        left, right = 0, n
        mid = left + (right - left) // 2

        while left < right:
            mid = left + (right - left) // 2
            if A[mid] < x:
                left = mid + 1
            else:
                right = mid
        return A[mid] == x
