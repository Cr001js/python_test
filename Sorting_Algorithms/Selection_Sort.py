# Selective sorting is quite simple; However, in most cases it has a better performance than bubble sorting. If you are going to choose one of these two methods, in most cases it can be said that selective sorting is a better option. In selective sorting, we divide our list or array into two parts. One of the subdivisions is sorted and the other is a subdivision that is still waiting for sorting. First, select the smallest element in the inappropriate subdivision and place it at the bottom of the subsidiary. Therefore, we regularly remove the smallest inappropriate element and place it at the bottom of the subdivision. This process will continue until all elements are transferred to the list regularly.
# :)

def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

a = [2, 7, 47, 88 , 1 ]

s = selection_sort(a)
print(s)