def quickSort(a: list, l: int, r: int):
    """
    Sorts an array using quicksort.
    - a is the list.
    - l is the left-most index.
    - r is the right-most index.
    Should output the array in nondecreasing (increasing???) order
    """
    if (l < r):
        s = hoarePartition(a,l,r)
        quickSort(a, l, s-1)
        quickSort(a, s+1, r)
    print(a)

def hoarePartition(a: list, l:int, r:int): 
    """
    Partitions the sublist.
    - subA: sub-list of the overall list. l = 0, r = n-1 of sublist.
    """

    # Get the left-most item in the list
    p = a[l]

    i = l+1 # Left-most element in the sublistlen(a)-1
    j = r # Right-most element in the sublist
    _swap(a,i,j)

    # while not x == repeat ... until x
    while not (i >= j):
        while not (a[i] >= p):
            i += 1
        while not (a[j] <= p):
            j -= 1
        _swap(a, i, j)
        print(f"hoare: {a}")
    
    _swap(a, i, j)
    _swap(a, l, j)
    return j

def _swap(a: list, idx1: int, idx2: int):
    tmp = a[idx1]
    a[idx1] = a[idx2]
    a[idx2] = tmp

myList = [9,2,33,77,18,99, -4]
listTwo = [1,2,3,4,5,6,2]
listThree = [0,1,6,2,3,1,10]
listFour = [9,8,7,6,5,4,3,2,1]

quickSort(myList, 0, len(myList)-1)
quickSort(listTwo, 0, len(listTwo) -1)
quickSort(listThree, 0, len(listThree)- 1)
quickSort(listFour, 0, len(listFour) - 1)
