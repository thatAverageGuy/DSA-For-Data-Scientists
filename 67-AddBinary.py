# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
def addBinary(a, b):
    carry = 0
    i, j = len(a)-1, len(b)-1
    result = []

    while i>=0 or j>=0 or carry:
        total = carry
        if i>=0:
            total+=int(a[i])
            i-=1
        if j>=0:
            total+=int(b[j])
            j-=1
        result.append(str(total%2))
        carry = total//2
    return ''.join(result[::-1])