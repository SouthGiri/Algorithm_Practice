ham = []
beve = []
for _ in range(3):
    ham.append(int(input()))
for _ in range(2):
    beve.append(int(input()))
print(min(ham) + min(beve) - 50)