
Start = input("Start with: ").rsplit(' ')
N = int(input("N: "))

Tribonacci = [int(Start[0]), int(Start[1]),int(Start[2])]

for i in range(3,N):
    Tribonacci.append((Tribonacci[i -3] + Tribonacci[i -2] + Tribonacci[i-1]))

print(Tribonacci[len(Tribonacci) - 1])