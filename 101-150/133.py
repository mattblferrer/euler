from math import log2, sqrt


# creates a Sieve of Eratosthenes array of size n
def soe(n):
    # for 0 and 1
    isPrimeList[0] = False
    isPrimeList[1] = False

    # for even numbers
    multiple = 4

    while multiple < n:
        # assign multiples of 2 as not being prime
            isPrimeList[multiple] = False  
            multiple += 2

    # for 3
    multiple = 9
    
    while multiple < n:
        # assign multiples of 3 as not being prime
            isPrimeList[multiple] = False  
            multiple += 3

    # for 6k +- 1
    for i in range(5, iterlimit+2, 6):  
        multiple = i*i  # initialize to i^2 for optimization

        while multiple < n:
            # assign multiples of i as not being prime
            isPrimeList[multiple] = False  
            multiple += i

        multiple = (i+2)*(i+2)  # initialize to i^2 for optimization

        while multiple < n:
            # assign multiples of i as not being prime
            isPrimeList[multiple] = False  
            multiple += (i+2)


# create a sieve of Eratosthenes
limit = 100000
iterlimit = int(sqrt(limit)) + 1
isPrimeList = [True]*(limit + 1)
soe(limit) 

# declare variables
nonPrimeSum = 0
primeSet = set()

# main loop
for i in range(limit):
    if isPrimeList[i]:
        isFactor = False

        for j in range(int(log2(i))+1): 
            if pow(10, 10**j, i) == 1:  # check for prime factors of repunits
                isFactor = True
                primeSet.add(i)
                break

        if not isFactor or i == 3:
            nonPrimeSum += i

# print result
print("Sum of all the primes that will never be a factor:", nonPrimeSum)