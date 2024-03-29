"""
The GCD of 1504170715041707 and 4503599627370517 is 1, so they must have a 
modular multiplicative inverse.
"""


def mod_mult_inv(num: int, x: int) -> int:
    """returns the modular multiplicative inverse of num mod x"""
    r0, r1 = x, num
    t0, t1 = 0, 1

    # extended Euclidean algorithm
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 % r1  # remainders after Euclidean division
        t0, t1 = t1, (t0 - t1*q) % x
        
    return t0
        

def main():
    # declare variables
    a = coin = maximum = eulercoin_sum = 1504170715041707  # starting Eulercoin
    m = 4503599627370517

    # find first Eulercoins
    for i in range(1, 42298634):  # 42298634 found through brute force search
        coin += a
        if coin >= m:
            coin -= m

        if maximum > coin:
            maximum = coin
            eulercoin_sum += coin

    # find modular multiplicative inverse
    inv = mod_mult_inv(a, m)

    # calculate later Eulercoins
    coin = 0
    minimum = m

    for i in range(1, maximum):
        coin += inv
        if coin >= m:
            coin -= m
        
        if minimum > coin:
            minimum = coin 
            eulercoin_sum += i

    # print result
    print(f"The sum of all Eulercoins is {eulercoin_sum}")


if __name__ == "__main__":
    main()
