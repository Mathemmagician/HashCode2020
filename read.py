
books, numLibs, days = [int(k) for k in input().split()]
scores = [int(k) for k in input().split()]
Libs = []

for i in range(numLibs):
    info = {}
    tmp = [int(k) for k in input().split()]
    info['numBooks'] = tmp[0]
    info['numDays'] = tmp[1]
    info['shippingTotal'] = tmp[2]

    info['books'] = [int(k) for k in input().split()]


