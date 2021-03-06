for i in range(100000, 1000000):  # number has to have at least 6 digits
    # digits in i
    digits = set()
    for digit in str(i):
        digits.add(digit)

    # used digits across i, 2i, 3i, 4i, 5i, 6i
    totalUsedDigits = set()
    for j in range(1, 7):
        for digit in str(i*j):
            totalUsedDigits.add(digit)

    # check if digits used are the same
    if len(digits) == 6 and len(totalUsedDigits) == 6:
        print(i)
