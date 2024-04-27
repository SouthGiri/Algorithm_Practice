import sys
input = sys.stdin.readline

from math import ceil

a, b, v = map(int, input().split())
print(ceil((v-b) / (a-b)))