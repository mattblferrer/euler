def main():  
    # declare variables
    limit = 999  # only calculate below 1000

    # calculate sum of divisible by 3, 5, and 15
    sum3 = 3 * (limit // 3) * (limit // 3 + 1)
    sum5 = 5 * (limit // 5) * (limit // 5 + 1)
    sum15 = 15 * (limit // 15) * (limit // 15 + 1)
    output = (sum3 + sum5 - sum15) // 2

    # print result
    print(output)


if __name__ == "__main__":
    main()
