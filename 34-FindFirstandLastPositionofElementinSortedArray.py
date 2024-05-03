# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 = nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

def searchRange(nums, target):
    ## Cheap Python Trick
    # start = -1
    # end = -1
    # try:
    #     start = nums.index(target)
    # except:
    #     return [start, end]
    # nums = nums[::-1]
    # end = (len(nums)-1) - nums.index(target)
    # return [start, end]
    
    # Actual Solution
    # We will do binary search with some extra conditions
    left = 0
    right = len(nums) - 1

    start = -1
    while left<=right:
        mid = (left + right)//2
        if target==nums[mid]:
            #
            if mid-1>=0 and nums[mid-1]!=target or mid==0:
                start = mid
            right=mid-1
        elif target<nums[mid]:
            right = mid-1
        else:
            left = mid+1

    end = -1
    left = 0
    right = len(nums) - 1
    while left<=right:
        mid = (left + right)//2
        if target==nums[mid]:
            if mid+1<len(nums) and nums[mid+1]!=target or mid==len(nums)-1:
                end = mid
            left = mid+1
        elif target<nums[mid]:
            right = mid-1
        else:
            left = left+1

    return [start, end]