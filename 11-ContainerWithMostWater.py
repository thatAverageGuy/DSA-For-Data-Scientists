# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

def maxArea(height):
    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        # width of the container
        width = right - left
        # we can only use up until the height of shorter bar
        usable_length = min(height[left], height[right])
        # calculate area of container
        area = max(area, usable_length*width)

        # if left bar is smaller, then we increase the left by one since to increase area further
        # we need to increase the value of length.
        if height[left]<height[right]:
            left+=1
        
        # if right bar is smaller, then we decrease the right by one.
        else:
            right-=1
        
    return area