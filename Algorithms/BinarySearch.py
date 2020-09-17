class BinarySearch:
    def binSearch(self,A,x):
        n = len(A)-1 #Don't forget the -1, common bug
        if n == 0:
            raise Exception("Array must contain some elements")

        l,r = 0,n

        while l <= r:
            mid = l + (r - l)//2
            if A[mid] == x:
                return True
            elif A[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def binSearchRightmost(self,A,x):
        n = len(A)
        if n == 0:
            raise Exception("Array must contain some elements")

        l,r = 0,n

        while l < r:
            mid = l + (r-l)//2
            if A[mid] > x:
                r = mid - 1
            else:
                l = mid
        return A[r-1] == x
    
    def binSearchLeftmost(self,A,x):
        n = len(A)
        if n == 0:
            raise Exception("Array must contain some elements")

        l,r = 0,n

        while l < r:
            mid = l + (r-l)//2
            if A[mid] < x:
                l = mid + 1
            else:
                r = mid
        return A[] == x