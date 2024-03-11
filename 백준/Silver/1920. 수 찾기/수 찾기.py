import sys
input = sys.stdin.readline

n = int(input())
nset= set(map(int, input().split()))

m = int(input())
mli = list(map(int, input().split()))
mset = set(mli)
mset = mset.intersection(nset)

for i in mli:
    if i in mset:
        print(1)
    else:
        print(0)
