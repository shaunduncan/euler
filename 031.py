# coding: utf8
"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count(coins, amount):
    """
    Given an amount we have, see the combinations of coins it takes to make change
    """
    # We have reached the target
    if amount == 0:
        return 1

    # We have gone overboard
    if amount < 0:
        return 0

    total = 0

    # For each coin, figure out the maximum multiplier such that coin X num <= amount
    # Then, do a recursive coint on the current amount, minus the coin times a multiplier
    # and count the ways to figure out the remaining coins
    for i, c in enumerate(coins):
        max = amount / c
        new_coins = coins[i+1:]

        for x in xrange(1, max + 1):
            total += count(new_coins, amount - (x * c))

    return total

print count(coins, 200)
