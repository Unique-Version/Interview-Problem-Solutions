# For an array, inversion count indicates how far (or close) the array is from being sorted.
# If array is already sorted then inversion count is 0. If array is sorted in reverse order
# that inversion count is the maximum.
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

# Difficulty -> Medium

# Asked in Adobe,Amazon,Flipkart,Walmart

# There can be a lot of approaches to solve this problem. A Naive approach would be to
# loop through the entire array checking whether the current element is greater than the other elements
# which is the condition for inversion. This would take O(n^2) time.

# An efficient approach would be to use merge sort technique which is a divide and conquer paradigm.
# We can simply divide the array and merge it back checking the inversion condition for each left and right
# sub-array. The total number of inversions will be the inversions encountered in left half , right half and
# in the merge step. This would run in O(n*log(n)) time. But there are more better methods out there such as using
# Fenwick trees.


# Function for merging arrays divided using merge_sort function modified to count inversions
def merge(arr, start, end):
    
    # find the middle element
    mid = (start + end) // 2

    # declaring a temp array for sorting
    tmp = [0] * len(arr)

    # a pointer at the start of arr
    i = start

    # a pointer at (mid+1) of arr
    j = mid + 1

    # another pointer (used for tmp) which points to start of arr
    k = start

    # count the number of inversions in merge step
    inversion_count = 0

    # while i reaches mid and j reaches the end
    while i <= mid and j <= end:

        # for sorted output, we need to pick the smallest between ith and jth
        # (if i is smaller)
        if arr[i] <= arr[j]:

            # place the element in tmp array
            tmp[k] = arr[i]

            # advance the pointers by 1
            k += 1
            i += 1

        else:

            # do the same if j is smaller
            tmp[k] = arr[j]

            # update the inversion count
            inversion_count += (mid - i + 1)

            # advance the pointers
            k += 1
            j += 1

    # if one of the array is exhausted we need to copy the remaining elements to tmp
    # (if ith part is bigger)
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1

    # do the same if jth part is bigger
    while j <= end:
        tmp[k] = arr[j]
        k += 1
        j += 1

    # at this point tmp is sorted so copy all the elements of tmp to arr
    for index in range(start, end + 1):
        arr[index] = tmp[index]

    return inversion_count


# enhanced merge_sort function to count inversions
def merge_sort(arr, start, end):
    
    # to count number of inversion
    inv_count = 0

    # if there is only one element then no need to sort
    if start < end:
        # find the middle index
        mid = (start + end) // 2

        # recursive call to merge_sort for one half of array(left) and store the inversion count
        inv_count = merge_sort(arr, start, mid)

        # recursive call to merge_sort for the other half of the array and store the inversion count
        inv_count += merge_sort(arr, mid + 1, end)

        # merge the arrays and add the inversion count for the merge step
        inv_count += merge(arr, start, end)

    # return the count
    return inv_count


# Driver Code
arr = [2, 4, 1, 3, 5]
inversion_count = merge_sort(arr, 0, len(arr) - 1)
print(f"Number of inversions are: {inversion_count}")


# Time Complexity : O(n*log(n))
# Space Complexity : O(n)
