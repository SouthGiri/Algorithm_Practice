import sys
input = sys.stdin.readline

# 진실 or 과장
# 되도록 과장 / 진실 아는 사람 있으면 진실
# 과장 말할 수 있는 파티 최대수

# 사람 수 N 파티 수 M
N, M = map(int, input().split())
true = set(input().split()[1:])

party_list = []

for _ in range(M):
    party_list.append(set(input().split()[1:]))

for _ in range(M):
    for party in party_list:
        if party & true:
            true = true.union(party)

cnt = 0

for party in party_list:
    if party & true:
        continue
    cnt += 1

print(cnt)