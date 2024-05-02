# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s):
    ## We run a two pointer approach where the right pointer traverses the string and the left pointer is used to shift window if any repeats are occured and to calculate the window length.

    # Dictionary to hold the last index of each character. it will be like this {'a': 4} where 4 will be the last index of a.
    d = {}
    left = 0
    right = 0
    ans = 0
    ## Start with two pointers at the beginning.
    while left<len(s) and right<len(s):
        # current element. In the beginning both the pointers are at index 0.
        curr_element = s[right]
        # if the current element is already in the dictionary, update the left pointer to the next position after the last occurrence of the current element.
        if curr_element in d:
            left = max(left, d[curr_element]+1)
        # update the last index of the current element. if the element did not exist in dictionary, it will created. if it existed, its last seen position will be updated.
        d[curr_element]=right
        # ans is the maximum length of current window so far.
        ans = max(ans, right-left+1)
        # update the right pointer.
        right+=1
    return ans