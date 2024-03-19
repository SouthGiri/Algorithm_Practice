import sys
input = sys.stdin.readline

# dict 로 저장
num_name = dict()
name_num = dict()

n, m = map(int, input().split())
for i in range(1, n+1):
    pocket = input().rstrip()
    num_name[i] = pocket
    name_num[pocket] = i

# 문제 : 알파벳 -> 포켓몬 번호
# 숫자 -> 포켓몬 문자 출력
for _ in range(m):
    question = input().rstrip()
    try:
        num = int(question)
        print(num_name[num])
    except:
        print(name_num[question])