import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
cards_dict = Counter(cards)
m = int(input())
nums = list(map(int, input().split()))

# nums 원소에 대해 cards 에 몇 개가 있는지
for num in nums:
    if num in cards_dict.keys():
        print(cards_dict[num], end=' ')
    else:
        print(0, end=' ')
