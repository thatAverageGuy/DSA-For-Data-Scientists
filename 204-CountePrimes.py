# 204. Count Primes
# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106
def countPrimes(n):
    if n<2:
        return 0
    # initialize a boolean array of size n and set all elements to True i.e. every number is Prime.
    # then we know that 0 and 1 are not prime. So we set them to false.
    isPrime = [True]*n
    isPrime[0] = False
    isPrime[1] = False
    # Loop from 2 to sqrt(n) and check the boolean array isPrime and if its true
    # then set all the multiples of that element until n, to False.
    # This technique is also known as Sieve of Eratosthenes.
    for i in range(2, math.ceil(math.sqrt(n))):
        if isPrime[i]:
            for multiple in range(i*i, n, i):
                isPrime[multiple] = False
    
    return sum(isPrime)