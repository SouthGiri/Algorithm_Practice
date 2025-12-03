import sys
input = sys.stdin.readline

N = int(input())
words = {}
for _ in range(N):
    word = input().rstrip()

    for i in range(len(word)):
        w = word[i]
        digit = len(word) - i - 1
        if w in words:
            words[w] += 10**digit
        else:
            words[w] = 10**digit

alpha = sorted(words.values(), reverse=True)
ans = 0
num = 9
for ch in alpha:
    ans += ch*num
    num -= 1
print(ans)