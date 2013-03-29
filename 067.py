'''
Find the maximum sum of descending top to bottom

I'm doing this by inspecting the next row possibilities
to see what might yield the higher sum
'''

data = []
with open('data/067/triangle.txt') as fp:
    data = map(lambda x: map(int, x.split()), fp.read().strip().split('\n'))


total = 0
numrows = len(data)
last = 0

for i, row in enumerate(data):
    if len(row) == 1:
        total += row[0]
        continue

    a, b = row[last:last + 2]

    # Inspect to see which would yield a higher sum on the next round
    if i < numrows - 1:
        al, ar = data[i + 1][last], data[i + 1][last + 1]
        bl, br = data[i + 1][last + 1], data[i + 1][last + 2]

        if max(a + al, a + ar) > max(b + bl, b + br):
            print '[L]', a, b, '|', (a + al), (a + ar), '<>', (b + bl), (b + br)
            total += a
        else:
            print '[R]', a, b, '|', (a + al), (a + ar), '<>', (b + bl), (b + br)
            total += b
            last += 1
    else:
        # Last row, just get the max
        print a, b, total
        print row
        total += max(a, b)


print total
