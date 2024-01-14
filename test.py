import numpy as np 

import matplotlib.pyplot as plt

def bubbleSort(arr):
    xs = np.arange(0,len(arr),1)
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    plt.bar(xs, arr)
    plt.savefig(r"C:\Users\Rafal\OneDrive\Dokumenty\GitHub\AiSD\lista5\frames\fig0")
    plt.clf()

    n = 0

    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                plt.bar(xs, arr)
                plt.savefig(r"C:\Users\Rafal\OneDrive\Dokumenty\GitHub\AiSD\lista5\frames\fig" + str(n))
                n += 1
                plt.clf()
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return 


array = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(array)
print(array)
plt.bar(np.arange(0,len(array),1), array)
plt.savefig(r"C:\Users\Rafal\OneDrive\Dokumenty\GitHub\AiSD\lista5\frames\fig_k")