# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwo(l1, l2):
    l3 = ListNode()
    l3_head = l3
    while l1 and l2:
        if l1.val <= l2.val:
            l3.next = l1
            l1 = l1.next
        else:
            l3.next = l2
            l2 = l2.next
        l3 = l3.next    
    while l1:
        l3.next = l1
        l1 = l1.next
        l3 = l3.next
    while l2:
        l3.next = l2
        l2 = l2.next
        l3 = l3.next
    
    l3_head = l3_head.next
    return l3_head

def mergeKLists(lists):
    if not lists:
        return None
    i = 0
    j = len(lists) - 1
    last = j
    while last!=0:
        i = 0
        j = last
        while j>i:
            lists[i] = mergeTwo(lists[i], lists[j])
            i+=1
            j-=1
            last = j
    
    return lists[0]