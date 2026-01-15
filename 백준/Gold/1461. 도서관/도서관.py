import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

minus = sorted([-x for x in data if x < 0])
plus = sorted([x for x in data if x > 0])

first = True
ans = 0

while len(minus) > 0 or len(plus) > 0:
    if not plus or minus and minus[-1] > plus[-1]:
        flag = 'minus'
    else:
        flag = 'plus'
    
    if first:
        weight = 1
        first = False
    else:
        weight = 2
        
    if flag == 'minus':
        ans += minus[-1] * weight
        minus = minus[:-M]
    else:
        ans += plus[-1] * weight
        plus = plus[:-M]

print(ans)