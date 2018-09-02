#!/usr/bin/env python3
import calendar

cal = calendar.Calendar()


def todigits(i):
    return [int(d) for d in str(i)]


def daysinmonth(year, month):
    return [(todigits(month) + todigits(x)) for x in cal.itermonthdays(year, month) if x != 0]


def digitsofpi(filename):
    output = []
    with open(filename, 'r') as f:
        for line in f:
            for ch in line[2:]:
                output.append(int(ch))
    return output


def digitsinyear(year):
    return [daysinmonth(year, month) for month in range(1, 13)]


daydigits = set()
for dates in digitsinyear(2018):
    for day in dates:
        daydigits.add( tuple(day) )

alldays = daydigits.copy()

pi = digitsofpi(r'100000.txt')
idx = 0
while idx < len(pi) and len(daydigits) > 0:
    daydigits = [date for date in daydigits if tuple(pi[idx:idx+len(date)]) != date]
    idx += 1

print("Not Found ", len(daydigits))
print("Total ", len(alldays), " in  ", idx)
