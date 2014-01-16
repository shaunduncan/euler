"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from itertools import imap, ifilter


def is_palindrome(x):
    return x == x[::-1]


# Itertools to the rescue. Filter palindromic integers. Convert to binary string.
# Filter palindromic binary strings. Convert to integer. Sum.
print sum(
    imap(
        lambda x: int(x, 2),
        ifilter(
            is_palindrome,
            imap(
                lambda x: '{0:b}'.format(int(x)),
                ifilter(
                    is_palindrome,
                    imap(str, xrange(1000000))
                )
            )
        )
    )
)

# TODO: Can this be done by _generating_ palindromic binary strings? This is probably the "correct" way
