# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        
        # loop through RHS of cur_index
        for j in range(cur_index, len(arr)): # second to last for above loop, not this one!
            rhs_index = j
            # if the value of the smallest index is more than value of rhs_index
            # smallest index = rhs_index

            print(arr[smallest_index], " > ", arr[rhs_index], "?")
            if arr[smallest_index] > arr[rhs_index]:
                smallest_index = rhs_index
                print("Yes! New smallest index:", smallest_index, ": ", arr[smallest_index])
            else:
                print("Nope, smallest index is still:", smallest_index, ": ", arr[smallest_index])

        # TO-DO: swap
        # now I have the smallest_index and cur_index
        # placeholder? value of smallest_index = cur_index and cur_index = smallest_index
        # placeholder holds smallest_index value
        placeholder = arr[smallest_index]
        print("placeholder", placeholder, "cur_index", cur_index, arr[cur_index])
        # smallest_index gets cur_index value
        # cur_index value gets smallest_index value FROM placeholder
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = placeholder

    print(arr)
    return arr

# testArr = [3, 2, 4, 0]
# selection_sort(testArr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    print("start: ", arr)

    j = 0
    swap = 0

    while True:
        i = j
        cur_index = i
        next_index = i+1
        last_index = (len(arr) - 1)
        if len(arr) == 0:
            break
        elif arr[cur_index] == arr[last_index]: # if this is the last index
            if swap == 0: # and no swaps have occurred
                break
            elif swap > 0: # and swaps HAVE occurred
                j = 0 # start at beginning
                swap = 0 # start fresh swap count
                continue
        if arr[cur_index] > arr[next_index]:
            hold = arr[next_index]
            arr[next_index] = arr[cur_index]
            arr[cur_index] = hold
            swap = swap+1
            continue
        else:
            j = i+1
            continue
    
    return arr

bubbleArr = [1, 4, 3, 0, 2]
print(bubble_sort(bubbleArr))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr