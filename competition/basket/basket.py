"""
author: mertkosan
createdAt: 1/20/2018
"""
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    n_str = raw_input()
    n_str_reverse = n_str[::-1]

    number = int(n_str)
    number_rev = int(n_str_reverse)

    if number == number_rev:
        print "No"
    elif is_prime(number) and is_prime(number_rev):
        print "Yes"
    else:
        print "No"
