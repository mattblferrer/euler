# declare variables
n = 100

# number of partitions for numbers 0, 1
partition_arr = [0, 1]
partition_arr.extend([0]*n)

# returns the number of ways to partition a number into a sum of positive 
# integers
def partition_number(num: int) -> int:
    if num == 1:  # 1 = 1
        return 1
    elif num < 1:  # no ways to partition non-positive integer
        return 0

    # greater than 1
    counter = 0
    difference_array = []  # numbers to subtract from num
    difference = 0
    num2 = num  # store num for final evaluation

    # numbers for Euler's pentagonal number theorem
    while num > 0:
        counter += 1
        is_even = (counter % 2 == 0)
    
        difference += counter // 2 if is_even else counter
        num -= counter // 2 if is_even else counter

        difference_array.append(difference)

    num = num2  # reset num

    if sum(difference_array) > num:  # check for overflow in list
        difference_array.pop()  # remove last element

    # evaluate partition number
    partitions = 0

    for i, diff in enumerate(difference_array):
        p = partition_arr[num - diff]
        partitions += p if i % 4 < 2 else -p

    # return final partition number
    return partitions


# fill out partition array
for i in range(2, n+2):
    partition_arr[i] = partition_number(i)

# print result
print(f"The number 100 can be written as the sum of at least two integers in \
{partition_arr[n+1] - 1} ways")
