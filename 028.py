"""
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101. What is the sum
of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

values = set()

for n in xrange(1, 1002, 2):
    sq = n ** 2

    # The value of n^2 is always present and up the right diagonal
    values.add(sq)

    # Figure out the other corners going backwards by consecutively subtracting n-1 from n^2
    for i in xrange(1, 4):
        val = sq - (i * (n - 1))

        if val > 0:
            values.add(val)

print sum(values)
