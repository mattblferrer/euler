"""
Primes of the form (x^4-y^4)/(x^3+y^3) are also the primes of the form
x^2+(x+1)^2. 
"""

# test for composite
def _try_composite(a: int, d: int, n: int, s: int) -> bool:
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True  # n  is definitely composite
 

# Miller-Rabin primality test
def is_prime_mr(n: int) -> bool:
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    else:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19, 23))

_known_primes = [2, 3]


# declare variables
limit = 5*10**15
num_primes = 0
lower_square = 1
lower_diff = 3

# check if x^2+(x+1)^2 is prime
for upper in range(2, 5*10**7 + 1):  # iterate through all (x+1)^2
    upper_square = upper*upper  # calculate (x+1)^2
    prime = lower_square + upper_square

    if is_prime_mr(prime):  # check if prime
        num_primes += 1

    # increment lower prime
    lower_square += lower_diff
    lower_diff += 2
    
    if upper % 100000 == 0:  # progress tracker
        print(upper)

# print result
print(f"Number of primes: {num_primes}")
