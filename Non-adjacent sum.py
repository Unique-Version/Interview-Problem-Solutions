# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing
# each of them is that adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.


# Asked in Google
# Difficulty -> Medium


# Approach:
# This problem basically asks you to find out the maximum profit from the non-adjacent houses.
# The idea we can use is that if a robber is at a certain index i then to be non-adjacent he can
# pick the (i+2) or (i-2) elements from that element as he cannot pick (i+1) and (i-1) elements which will be 
# adjacent and if we leave the current house then we can pick (i+1) or (i-1) elements. So the end solution will be
# maximum of both the cases. As the problem involves both properties of DP thus we can use bottom-up dp
# to solve this which takes O(N) time and space. But as we need only two elements at a single time so we
# can use a temp variable to achieve constant space.


def rob(arr):

    n = len(arr)
    
    # If the array is empty
    if arr == 0 or len(arr) == 0:
        return 0

    # if the array has length one
    if len(arr) == 1:
        return arr[0]
    
    # Stores the first element
    prev2 = arr[0]
    
    # stores the maximum of first two
    prev1 = max(arr[0], arr[1])

    # Traversing the whole list from 2 as we have already takes 0 and 1 in account
    for i in range(2, n):
    
        # store prev1 into temp
        temp = prev1
        
        # choices we have
        prev1 = max(prev2 + arr[i], prev1)
        
        # store into prev2 to propagate the sum
        prev2 = temp

    # return the max sum
    return prev1


# Test cases
arr = [1, 2, 3, 1]
arr1 = [2, 7, 9, 3, 1]
print(rob(arr))
print()
print(rob(arr1))

# Time Complexity: O(N)
# Space Complexity : O(1)
