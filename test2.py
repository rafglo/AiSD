
from collections import deque
 
 
def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
def partition(a, start, end):
 
    # Pick the rightmost element as a pivot from the list
    pivot = a[end]
 
    # elements less than the pivot will go to the left of `pIndex`
    # elements more than the pivot will go to the right of `pIndex`
    # equal elements can go either way
    pIndex = start
 
    # each time we find an element less than or equal to the pivot,
    # `pIndex` is incremented, and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1
 
    # swap `pIndex` with pivot
    swap(a, pIndex, end)
 
    # return `pIndex` (index of the pivot element)
    return pIndex
 
 
# Iterative Quicksort routine
def iterativeQuicksort(a):
 
    # create a stack for storing sublist start and end index
    stack = deque()
 
    # get the starting and ending index of a given list
    start = 0
    end = len(a) - 1
 
    # push the start and end index of the array into the stack
    stack.append((start, end))
 
    # loop till stack is empty
    while stack:
 
        # remove top pair from the list and get sublist starting
        # and ending indices
        start, end = stack.pop()
 
        # rearrange elements across pivot
        pivot = partition(a, start, end)
 
        # push sublist indices containing elements that are
        # less than the current pivot to stack
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
 
        # push sublist indices containing elements that are
        # more than the current pivot to stack
        if pivot + 1 < end:
            stack.append((pivot + 1, end))
 
 
# Iterative Implementation of Quicksort
if __name__ == '__main__':
 
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
    iterativeQuicksort(a)
 
    # print the sorted list
    print(a)