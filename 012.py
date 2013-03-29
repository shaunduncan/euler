'''
n-th triangle number: sum 1..n

Find the first triangle number with >= 500 divisors
'''
import math
from itertools import count


for i in count():
    # Find the triangle number summing quickly
    triangle = i * (i + 1) / 2

    # Filter only divisors up to sqrt of triangle num
    # multiply by two for second half, add two for 1 and triangle number
    sqrt = int(math.sqrt(triangle))
    factors = filter(lambda x: triangle % x == 0, xrange(2, sqrt))
    num_factors = (len(factors) * 2) + 2

    if num_factors >= 500:
        print triangle
        break
