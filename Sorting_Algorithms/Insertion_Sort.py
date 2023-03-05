# This method is largely similar to the method of sorting the game cards that most people do instinctively. In each repetition, an element is removed from the array. Then the position of that element is found in the array if it is tidy. This process continues until all the input elements in the array are regularly found.
# =)

def insertion_sort(arr, simulation=False):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr

a = [4, 7, 4, 9, 2, 8, 3, 1]
s = insertion_sort(a)
print(s)