import sys
input = sys.stdin.readline

people_dict = dict()
u, n = map(int, input().split())
for _ in range(n):
    name, price = input().split()
    if int(price) <= u:
        people_dict[price] = people_dict.get(price, list()) + [name]

min_count = min([len(i) for i in people_dict.values()])
min_key = min([int(i) for i in people_dict.keys() if len(people_dict[i]) == min_count])

print(people_dict[str(min_key)][0], min_key)