# 941. Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 
# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104


def validMountainArray(arr):
        
    ## Approach 1
        ## Keep counting until there is a strictly increasing order.
        # i = 1
        # while i<len(arr) and arr[i]>arr[i-1]:
        #     i+=1

        ## If i does not move it means peak is at 0th index or if the i is at last index, it means the array only increasing and is not mountain.
        # if i==1 or i==len(arr):
        #     return False

        ## Keep counting until there is a strictly decreasing order, starting from the last point where the strictly increasing order ended.
        # while i<len(arr) and arr[i]<arr[i-1]:
        #     i+=1

        ## If we reached the end of the array, it means the array is a mountain.
        # return i==len(arr)

    # Approach 2
        # Count from both sides and stop where strictly increasing or strictly decreasing order stops. 
        # Check if the left peak is same as right peak and left peak is not at index 0 and right peak is not at last index.

        i=0
        while i<len(arr)-1 and arr[i]<arr[i+1]:
            i+=1

        j = len(arr)-1
        while j>0 and arr[j]<arr[j-1]:
            j-=1

        if i>0 and i==j and j<len(arr)-1:
            return True
        else:
            return False