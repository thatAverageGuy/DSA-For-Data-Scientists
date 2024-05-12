# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    h1 = list1
    h2 = list2

    if h1 and not h2:
        return h1
    if h2 and not h1:
        return h2

    newList = ListNode()
    h3 = newList
    while h1 and h2:
        if h1.val <= h2.val:
            h3.next = h1
            h1 = h1.next
        else:
            h3.next = h2
            h2 = h2.next
        h3 = h3.next

    if h1 is None:
        h3.next = h2
    elif h2 is None:
        h3.next = h1

    return newList.next