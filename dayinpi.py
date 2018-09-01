import calendar
import collections

cal = calendar.Calendar()


def todigits(i):
    return [int(d) for d in str(i)]


def daysinmonth(year, month):
    return [(todigits(month) + todigits(x)) for x in cal.itermonthdays(year, month) if x != 0]

# for date in daysinmonth(2018, 5):
#     print(date)

def digitsofpi(filename):
    output = []
    with open(filename, 'r') as f:
        for line in f:
            for ch in line[2:]:
                output.append(int(ch))
    return output

def digitsinyear(year):
    return [daysinmonth(year, month) for month in range(1, 13)]


daydigits = []
dayanswers = collections.OrderedDict()
for dates in digitsinyear(2018):
    for day in dates:
        dayanswers[tuple(day)] = False
        daydigits.extend(dates)

dayindexes = [0] * len(dayanswers.keys())

pi = digitsofpi(r'100000.txt')
for idx in range(len(pi)):
    for date in dayanswers.keys():
        numdigits = len(date)
        sliceofpi = pi[idx:idx+numdigits]
        if tuple(sliceofpi) == date:
            dayanswers[date] = True
        # print("Comparing ", tuple(sliceofpi), " and ", date)

# print(dayanswers)
found = 0
notfound = 0
for dateTuple in dayanswers.keys():
    answer = dayanswers[dateTuple]
    if answer:
        found += 1
    else:
        notfound += 1

print("Found ", found)
print("Not Found ", notfound)
print("Total ", found+notfound)
