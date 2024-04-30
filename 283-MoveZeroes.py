# Leetcode 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

def moveZeroesToEnd(nums):
    # Loop through the list and for every non-zero element encountered, place them one-by-one from zeroth position.
    count = 0
    for num in nums:
        if num!=0:
            nums[count]=num
            count+=1

    #Set all the remaining positions from count till the end of list to zero.
    for j in range(count, len(nums)):
        nums[j]=0

    return nums

def moveZeroesToFront(nums):
    # Reverse Loop through the list and for every non-zero element encountered, place them one-by-one from last position.
    count=len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if nums[i]!=0:
            nums[count]=nums[i]
            count-=1
    # Set all the remaining positions from 0 to count to zero.
    for i in range(0, count+1):
        nums[i]=0

    return nums