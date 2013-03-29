'''
Find the sum of the digits of 100!
'''
import math

print sum(int(n) for n in str(math.factorial(100)))
