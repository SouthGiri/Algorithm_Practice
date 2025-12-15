import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ans = []
common = set(A) & set(B)

if len(common) == 0:
    print(0)
else:
    while common:
        max_num = max(common)
        ans.append(max_num)

        idx_A = A.index(max_num)
        idx_B = B.index(max_num)

        A = A[idx_A+1 : ]
        B = B[idx_B+1 : ]

        common = set(A) & set(B)

    print(len(ans))
    print(*ans)