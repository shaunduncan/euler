'''
Find the smallest positive integer that can be evenly divided by
the numbers [1,20]

This is restated as LCM(1..20)
'''

from util import lcm


# Accumulate LCM values
print reduce(lcm, xrange(1, 20))
