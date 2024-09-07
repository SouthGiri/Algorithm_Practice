import sys
input = sys.stdin.readline


n = int(input())
song = input().rstrip()

alpha = [0 for _ in range(26)]

for s in song:
    if s != ' ' and s!=',' and s!='.':
        alpha[ord(s)%97] += 1
        
print(max(alpha))