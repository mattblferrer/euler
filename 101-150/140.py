def main():
    # declare variables
    limit = 30
    # found using Diophantine solution to 5x^2 + 14x + 1 = y^2
    x_choices = [2, 0, 0, -4, -3, -3]
    y_choices = [-7, -1, 1, 5, 2, -2]
    nuggets = {2, 5}  # store nuggets generated by recursive formula

    # iterate through all possible choices of x, y in choices above
    for x, y in zip(x_choices, y_choices):
        for _ in range(limit):
            x, y = -9 * x + 4 * y - 14, 20 * x - 9 * y + 28
            nuggets.add(x)

    # remove negatives and numbers that are too big
    nuggets = [i for i in sorted(nuggets) if i > 0][:limit]
    
    # print result
    print(sum(nuggets))


if __name__ == "__main__":
    main()
