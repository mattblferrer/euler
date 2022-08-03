# returns the prime factors of num (non-repeating)
def prime_factorize(num):
    factors = set()

    while num % 2 == 0:  # for only even prime
        factors.add(2)
        num //= 2

    while num % 3 == 0:  # for 3
        factors.add(3)
        num //= 3

    for i in range(6, int(num ** 0.5) + 3, 6):  # for 6k +- 1
        while num % (i-1) == 0:
            factors.add(i-1)
            num //= (i-1)
            
        while num % (i+1) == 0:
            factors.add(i+1)
            num //= (i+1)

    if num != 1:
        factors.add(num)

    return factors


# returns the Euler's totient of the number num using Euler's product formula
def totient(num):
    p_factors = prime_factorize(num)
    phi = num  # totient
    for factor in p_factors:
        phi = phi * (factor-1)//factor

    return phi


# declare variables
limit = 1000000
maximumRatio = 0
maximumN = 0

# main loop
for n in range(1, limit+1):
    ratio = n/totient(n)

    # compare with maximum ratio
    if ratio > maximumRatio:
        maximumRatio = ratio
        maximumN = n

# print output
print("The value of n for which n/phi(n) is at a maximum is {}".format(maximumN))
print("The maximum value of n/phi(n) is {}".format(maximumRatio))
