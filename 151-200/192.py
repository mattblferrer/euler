from decimal import Decimal, getcontext
getcontext().prec = 80  # 80 decimal digits of precision


# returns the closest approximation of the sqrt of num
def closest_approx_sqrt(num: int, bound: int) -> int:
    # convert to Decimal class for higher precision
    num = Decimal(num)
    sqrt_num = num.sqrt()  # whole number part
    fsqrt_num = sqrt_num % 1  # fractional part only
    n1, d1, n2, d2 = Decimal(0), Decimal(1), Decimal(1), Decimal(1)

    # close in on approximation using Farey sequence
    while True:
        med_n, med_d = n1+n2, d1+d2  # mediant of n1/d1 and n2/d2

        # check if bound is exceeded
        if med_d >= bound:
            break

        # narrow down approximations
        med = med_n / med_d
        if fsqrt_num > med:
            n1, d1 = med_n, med_d
        elif fsqrt_num < med:
            n2, d2 = med_n, med_d
        
    # compare differences and pick which denominator to return 
    diff_1 = abs(fsqrt_num - Decimal(n1)/Decimal(d1))
    diff_2 = abs(fsqrt_num - Decimal(n2)/Decimal(d2))

    return d2 if diff_1 > diff_2 else d1


def main():
    # declare variables
    d_limit = 10**12  # upper bound for denominator
    sum_d = 0
    n_limit = 100_000
    squares = {i*i for i in range(int(n_limit ** 0.5) + 1)}

    # test if code is correct for test cases
    print("Test cases: ")
    print(f"sqrt(13), bound 20: {closest_approx_sqrt(13, 20)}")
    print(f"sqrt(13), bound 30: {closest_approx_sqrt(13, 30)}", end="\n\n")

    # loop through all non-squares below limit
    for n in range(2, n_limit + 1):
        if n not in squares:
            sum_d += closest_approx_sqrt(n, d_limit)
        if n % 10000 == 0:  # progress tracker
            print(n)

    # print result
    print(f"Sum of denominators: {sum_d}")


if __name__ == "__main__":
    main()
