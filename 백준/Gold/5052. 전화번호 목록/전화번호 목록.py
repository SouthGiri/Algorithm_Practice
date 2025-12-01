T = int(input())
for _ in range(T):
    N = int(input())
    phones = []
    flag = 'YES'
    for _ in range(N):
        phones.append(input())
    phones.sort()

    for idx in range(N-1):
        if phones[idx] == phones[idx+1][:len(phones[idx])]:
            flag = 'NO'
            break

    print(flag)