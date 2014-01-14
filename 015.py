# Pascal's triangle. The nth middle element. Generate a full triangle until
# we have the 20th middle element
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
