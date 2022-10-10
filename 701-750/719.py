"""
All S-numbers are congruent to 0 or 1 mod 9.
"""
from math import sqrt


# checks if a square number is an S number
def is_s_number(sqr: int, index: int):
    # declare variables
    string = str(sqr)
    length = len(string) - 1
    index_length = len(str(index))
    formatting = f"0{length}b"  # to format to binary

    for subset_index in range(1, 2**length):
        if subset_index.bit_count() <= index_length:  # <= split limit
            subset_b = format(subset_index, formatting)

            # get subset of index subset_b and add terms
            split_index = [0]
            split_index.extend([i for i, d in enumerate(subset_b, start=1) if d == '1'])
            split_index.append(length + 1)

            # split number according to split subset
            split = [int(string[i:j]) for i, j in zip(split_index, split_index[1:])]
            n_sum = sum(split)

            # splitting number check
            if n_sum == index:
                print(index, string, split)
                return True
    
    return False


def main():
    # declare variables
    limit = 10**12
    sqr_limit = int(sqrt(limit))
    sqr, index = 1, 1  # square and its square root (index)
    s_sum = 0  # sum of all S numbers (T(N))

    # main loop
    while index <= sqr_limit:
        if is_s_number(sqr := sqr + 16*index + 64, index := index + 8):  # 0 mod 9
            s_sum += sqr

        if is_s_number(sqr := sqr + 2*index + 1, index := index + 1):  # 1 mod 9
            s_sum += sqr

    # print result
    print(f"T({limit}) = {s_sum}")
