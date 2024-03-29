from math import log10


# generates the log base 10 of the convergents of square root of 2
def convergents(terms: int) -> int:
    a, b = 3, 2  # starting term a/b is 3/2
    longer_num = 0  # number of fractions with longer numerator

    # generate next terms
    for _ in range(terms+1):
        a, b = a+2*b, a+b

        if int(log10(a)) > int(log10(b)):
            longer_num += 1

    return longer_num


# print output
output = convergents(1000)
print("The number of fractions where the numerator has more digits than the denominator is", output)
