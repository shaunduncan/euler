"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

+---+---+
|   |   |
+---+---+
|   |   |
+---+---+

"""

# Pascal's triangle. The nth middle element. Generate a full triangle until
# we have the 20th middle element. This is brute force, but whatever
rows = {}
results = []
i = 0

while len(results) <= 20:
    rows[i] = [1]

    if i > 0:
        for j in xrange(1, i):
            try:
                rows[i].append(rows[i-1][j-1] + rows[i-1][j])
            except IndexError:
                rows[i].append(1)

        rows[i].append(1)

    if len(rows[i]) % 2 == 1:
        results.append(rows[i])

    i += 1

print max(results[-1])
