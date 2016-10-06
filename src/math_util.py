from responses import InvalidUsage, Prime
from decimal import *
import math

# Set E constant & remove decimal
getcontext().prec = 170  # max precision for 5, 12
E = str(Decimal(1).exp()).replace('.', '')


def find_xth_prime(x, num_digits):
    '''
    Finds the xth num_digits prime in Euler's constant.
    If found, returns a Prime object containing, x, num_digits, its prime value, as well as the position it was found.
    If not found, raises an InvalidUsage ex
    '''
    prime_iters = 0

    for i in range(0, len(E) - num_digits):
        num = int(E[i:i + num_digits])
        if is_prime(num):
            prime_iters += 1
            if prime_iters == x:
                return Prime(x, num_digits, num, i)

    raise InvalidUsage("Unable to calculate")


def is_prime(num):
    '''Returns true if num is a prime'''
    if num > 2 and num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
