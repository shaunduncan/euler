'''
Find the largest palindrome made from the product of
two 3-digit integers
'''

start = 100
end = 1000
largest = 0

for a in reversed(xrange(start, end)):
    for b in reversed(xrange(start, a)):
        value = a * b

        if str(value) == str(value)[::-1]:
            largest = max(largest, value)

print largest
