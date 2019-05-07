# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print(f"merge({arrA}, {arrB})")
    print("elements", elements)
    merged_arr = [0] * elements
    print(f"merged_arr: {merged_arr}")
    # TO-DO
    i = 0
    j = 0
    k = 0

    for i in range(i, elements):
        print(f"arrA: {arrA}, arrB: {arrB}")
        if j >= len(arrA): # arrA is exhausted
            merged_arr[i] = arrB[k]
            k += 1
        elif k >= len(arrB): # arrB is exhausted
            merged_arr[i] = arrA[j]
            j += 1
        elif arrA[j] < arrB[k]: # arrA[j] is smaller
            merged_arr[i] = arrA[j]
            j += 1
            print(f"j: {j}")
        elif arrB[k] < arrA[j]: # arrB[k] is smaller
            merged_arr[i] = arrB[k]
            print(f"{k}")
            k += 1

            
    # loop thru elements
    # compare arrA values to arrB values to find smallest
    # replace value on merged arr? why not push onto empty arr?
    # use incremental variables to track array indices
    # i for merged arr
    # j and k for arrs
    # j++ or k++ respectively when value IS smaller
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
     # if length is > 1
        # split using [mid:] = rhs and [:mid] = lhs
        # mid = length/2
    if len(arr) > 1:
        mid = int(len(arr)/2)
        # call recursively to split
        lhs = merge_sort(arr[:mid])
        rhs = merge_sort(arr[mid:])
    # call merge(lhs,rhs)
        arr = merge(lhs, rhs)
    # else:
    return arr

print(merge_sort([0, 1, 5, 7, 3, 8]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
