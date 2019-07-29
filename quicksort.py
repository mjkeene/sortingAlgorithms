def quicksort(A):
    if len(A) < 2:
        return A
    else:
        less = []
        equal = []
        greater = []
        pivot = A[0]
        for num in A:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            elif num > pivot:
                greater.append(num)
        return quicksort(less) + equal + quicksort(greater)
