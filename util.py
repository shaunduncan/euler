import math


def even(num):
    '''
    Rather than writing a lambda every time for checking even numbers
    '''
    return num % 2 == 0


def odd(num):
    '''
    Rather than writing a lambda every time for checking odd numbers
    '''
    return num % 2 == 1


def fib(num):
    '''
    Calculates Fibonacci number by remembering past ones
    '''
    if num in fib._values:
        return fib._values[num]
    else:
        fibval = fib(num - 1) + fib(num - 2)
        fib._values[num] = fibval
        return fibval
fib._values = {0: 0, 1: 1}  # This will mean we only calculate fib(n) once


def collatz(n):
    '''
    Returns the next collatz number from n:
    if even(n): n / 2
    if odd(n): 3n + 1
    '''
    if n == 1:
        return 1
    if even(n):
        return n / 2
    else:
        return (3 * n) + 1


def is_prime(n):
    '''
    Checks if a number is prime by stopping at the first number that
    evenly divides up to sqrt of n
    '''
    return not any(n % i == 0 for i in xrange(3, int(math.sqrt(n)) + 1, 2))


def gcd(a, b):
    '''
    GCD using Euclidean algorithm:
    gcd(a, b) = gcd(b, a mod b)
    '''
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    '''
    Really just derived from:
    gcd(a, b) = (a * b) / lcm(a, b)
    '''
    return (a * b) // gcd(a, b)


def divisors(n):
    '''
    Find the unique divisors from [1,n). Note that this will include 1, but not n.
    Repeatedly lower the top-end limit as a divisor is found
    '''
    nums = {1}
    limit = n
    i = 2

    while i < limit:
        if n % i == 0:
            limit = n / i
            nums.update([i, limit])
        i += 1

    return nums


def sum_of_divisors(n):
    '''
    Find the sum of unique divisors from [1,n). Note that this will include 1, but not n.
    Repeatedly lower the top-end limit as a divisor is found
    '''
    return sum(divisors(n))
