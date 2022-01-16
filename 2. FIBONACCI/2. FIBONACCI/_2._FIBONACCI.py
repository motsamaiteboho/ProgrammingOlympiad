F = int(input("F = "))
S = int(input("S = "))
L = int(input("L = "))

Sequence = [F,S]

for i in range(2, L):
    Sequence.append((Sequence[i-2]+Sequence[i-1]))

print(Sequence);

