# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print(elements)
    merged_arr = [0] * elements
    # TO-DO
    # loop thru elements
    # compare arrA values to arrB values to find smallest
    # replace value on merged arr? why not push onto empty arr?
    # use incremental variables to track array indices
    # i for merged arr
    # j and k for arrs
    # j++ or k++ respectively when value IS smaller
    return merged_arr

print(merge([1], [2]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if length is > 1
        # split using [mid:] = lhs and [:mid] = rhs
        # mid = length/2
    # call recursively to split
    # call merge(lhs,rhs)
    # else:
    return arr


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
