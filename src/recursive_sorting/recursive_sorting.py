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
        if arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
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
        # split using [mid:] = lhs and [:mid] = rhs
        # mid = length/2
    if len(arr) > 1:
        mid = int(len(arr)/2)
        lhs = arr[mid:]
        rhs = arr[:mid]
    # call recursively to split
        merge_sort(lhs);
        merge_sort(rhs);
    # call merge(lhs,rhs)
        return merge(lhs, rhs)
    # else:
    return ("arr", arr)

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
