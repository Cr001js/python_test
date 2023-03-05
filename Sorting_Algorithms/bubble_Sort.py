# Bubble sorting is one of the algorithms that are usually presented in basic courses of computer science classes, as it clearly shows the way it is sorted and simultaneously understanding it is easy and easy. The bubble sorting steps are performed through a list and comparison of adjacent elements. In this process, when the elements are incorrect, they are replaced. This operation continues on the arrays as long as none of the two elements are incorrect.
# =)

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

a = [5, 3, 7, 2, 6, 1]
s = bubble_sort(a)
print(s)