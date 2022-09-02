from math import prod

def sum_factors(num):  # returns the sum of the factors of num
    check = num
    factors = []

    for i in [2, 3]:  # for 2 and 3
        power = 1
        cFactor = 1

        while num % i == 0:
            cFactor += i**power
            num //= i
            power += 1

        factors.append(cFactor)

    for i in range(6, int(num ** 0.5) + 3, 6):  # for 6k +- 1
        # 6k - 1
        power = 1
        cFactor = 1
        while num % (i-1) == 0:
            cFactor += (i-1) ** power
            num //= (i-1)
            power += 1

        factors.append(cFactor)
            
        # 6k + 1
        power = 1
        cFactor = 1
        while num % (i+1) == 0:
            cFactor += (i+1) ** power
            num //= (i+1)
            power += 1

        factors.append(cFactor)

        if num == 1:
            break

    if num != 1:
        factors.append(num+1)

    return prod(factors) - check
    

nonAbundantSum = 0  # sum of all the positive integers that can't be expressed as the sum of two abundant numbers
limit = 28123  # given parameter
canBeSum = [False]*limit
abundantList = [i for i in range(2, limit) if sum_factors(i) > i]  # calculate all abundant numbers below limit

for i in abundantList:  # calculate all numbers that can be sum of two abundant numbers
    for j in abundantList:
        if i+j-1 < limit:
            canBeSum[i+j-1] = True

for i in range(limit):  # add False numbers to sum
    if not canBeSum[i]:
        nonAbundantSum += (i+1)

print("The sum of all positive integers that can't be written as the sum of two abundant numbers is", nonAbundantSum)
