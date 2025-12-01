N = int(input())
data = set(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

for card in cards:
    print(1, end=' ') if card in data else print(0, end=' ')