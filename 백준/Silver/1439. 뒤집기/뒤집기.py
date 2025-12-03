import sys
input = sys.stdin.readline

string = input()
cnt0 = cnt1 = 0

for i in range(len(string)-1):
    if string[i] != string[i+1]:
        if string[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1

if string[-2] != string[-1]:
    if string[-2] == '0':
        cnt0 += 1
    else:
        cnt1 += 1

print(min(cnt0, cnt1))