'''
Find the number of Sundays that are on the first day of the month
between Jan 1, 1901 and Dec 31, 2000

Remember:
Leap years are year mod 4, unless a century then year mod 400
1 Jan, 1900 is a Monday
Sept, Apr, June, Nov -> 30 days
Rest -> 31 days
Feb -> 28 days (29 in leap year)

DOW Numbering: 0 == Sunday
'''

days_in_month = {
    365: (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
    366: (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
}


def days_in_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return 366
    elif year % 100 != 0 and year % 4 == 0:
        return 366
    else:
        return 365

# Starting from 1900
day_of_week = (1 + days_in_year(1900)) % 7
sundays = 0

for year in xrange(1901, 2001):
    for num_days in days_in_month[days_in_year(year)]:
        day_of_week = (day_of_week + num_days) % 7
        if day_of_week == 0:
            sundays += 1

print sundays
