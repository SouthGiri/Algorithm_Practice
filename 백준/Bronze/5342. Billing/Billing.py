import sys
input = sys.stdin.readline


key = ['Paper', 'Printer', 'Planners', 'Binders', 'Calendar', 'Notebooks', 'Ink']
val = [57.99, 120.5, 31.25, 22.5, 10.95, 11.2, 66.95]
office = dict(zip(key, val))
cost = 0

while True:
    item = input().rstrip()
    if item == 'EOI':
        break
    else:
        cost += office[item]
print('${}'.format(cost))