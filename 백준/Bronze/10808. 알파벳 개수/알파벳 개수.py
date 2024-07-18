ans = [0]*26
word = input().rstrip()
for w in word:
    ans[ord(w) - 97] += 1
print(*ans)