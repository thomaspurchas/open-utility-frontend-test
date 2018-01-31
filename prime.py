"""
Helper module that provides a prime sieve. Sieve implementation taken
from:
https://iamrafiul.wordpress.com/2013/04/28/sieve-of-eratosthenes-in-python/
"""

def sieve(n):
    """
    Calculate all primes up to n and return them in a list
    """

    not_prime = []
    prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
    return set(prime)
