# 78. Subsets
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [], [2, 3] -> [], [3] -> []
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [], [2, 3] -> [], [3] -> [3]
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [], [2, 3] -> [2], [3] -> [2]
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [], [2, 3] -> [2], [3] -> [2, 3]
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [1], [2, 3] -> [1], [3] -> [1]
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [1], [2, 3] -> [1], [3] -> [1, 3]
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [1], [2, 3] -> [1, 2], [3] -> [1, 2]
# index = 0 -> index 1 -> index 2
# [1, 2, 3] -> [1], [2, 3] -> [1, 2], [3] -> [1, 2, 3]
# index 1 -> index 2
# [1, 2, 3] -> [], [3] -> []
# index 1 -> index 2
# [1, 2, 3] -> [], [3] -> [3]
# index 1 -> index 2
# [1, 2, 3] -> [2], [3] -> [2]
# index 1 -> index 2
# [1, 2, 3] -> [2], [3] -> [2, 3]
# index 2
# [1, 2, 3] -> [], [3] -> []
# index 2
# [1, 2, 3] -> [3], [] -> [3]
#[[], [1], [2], [3], [1, 2], [1, 3], [1, 2, 3]]

def sol(nums, index, subset, ans):
    if index>=len(nums):
        ans.append(subset[:])
        return

    # Did not choose
    sol(nums, index+1, subset, ans)

    # # Did choose
    sol(nums, index+1, subset+[nums[index]], ans)
    
def subsets(nums):
    ans = []
    subset = []
    index=0
    sol(nums, index, subset, ans)
    
    return ans