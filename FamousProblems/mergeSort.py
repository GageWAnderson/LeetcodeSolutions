def mergeSort(A):
    if(len(A) > 1):
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        mergeSort(L)
        mergeSort(R)

        A.clear() #Not in place
        #merge(L,R)
        while(len(L) > 0 and len(R) > 0):
            if(L[0] <= R[0]):
                A.append(L.pop(0))
            else:
                A.append(R.pop(0))

        for elemL in L:
            A.append(elemL)

        for elemR in R:
            A.append(elemR)