def quickSort(a: list, l: int, r: int):
    """
    Sorts an array using quicksort.
    - a is the list.
    - l is the left-most index.
    - r is the right-most index.
    Should output the array in nondecreasing (increasing???) order
    """
    if (l < r):
        s = hoarePartition(a[l:r+1])
        quickSort(a, l, s-1)
        quickSort(a, s+1, r)
    print(a)

def hoarePartition(subA: list): 
    """
    Partitions the sublist.
    - subA: sub-list of the overall list. l = 0, r = n-1 of sublist.
    """

    # Get the left-most item in the list
    p = subA[0]

    i = 0 # Left-most element in the sublist
    j = len(subA)-1 # Right-most element in the sublist

    # while not x == repeat ... until x
    while not (i >= j):
        while not (subA[i] >= p):
            i += 1
        while not (subA[j] <= p):
            j -= 1
        _swap(subA, i, j)
        print(f"hoare: {subA}")
    
    _swap(subA, i, j)
    _swap(subA, 0, j)
    return j

def _swap(subA: list, idx1: int, idx2: int):
    tmp = subA[idx1]
    subA[idx1] = subA[idx2]
    subA[idx2] = tmp

myList = [9,2,-4,77]

quickSort(myList, 0, len(myList)-1)
