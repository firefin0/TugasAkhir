import random

def insertion_sort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        print(arr)

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    print(arr)

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        print('Loop {}'.format(i))

        # Last i elements are already in place
        for j in range(0, n-i-1):

            print(arr)

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)

n = int(input('Please Input (n):'))
arr = random.sample(range(1, n + 1), n)

# Driver code to test above
print('Insertion Sort:')
insertion_arr = arr.copy()
insertion_sort(insertion_arr)

# Driver code to test above
print('Bubble Sort:')
bubble_arr = arr.copy()
bubble_sort(bubble_arr)


"""
TODO:
* visualize sorting graph
"""
